from venv import logger
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from usercrud.serializers import UserSerializer
from usercrud.models import User
# Create your views here.


class UserView(APIView):
    def get(self, request,format=None):
        search = None
        users = None
        if "search" in request.GET:
            search = request.GET["search"]
            if search:
                users = User.objects.filter(name__icontains=search) \
                | User.objects.filter(email__icontains=search) \
                | User.objects.filter(contact__icontains=search)  \
                | User.objects.filter(id__icontains=search) 
        else:
            users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    def post(self, request,format=None):
        name =request.data
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class UseridView(APIView):
        def get_object(self, id):
            try:
                return User.objects.get(id=id)
            except User.DoesNotExist:
                raise Http404

        # Read
        def get(self, request, id, format=None):
            users= self.get_object(id)
            serializer = UserSerializer(users)
            logger.info("data retrieved successfully")
            return Response(serializer.data)      

        # Update
        def put(self, request, id, format=None):
            users= self.get_object(id) 
            serializer=UserSerializer(users,data=request.data) 
            if serializer.is_valid():
                serializer.save()  
            return Response(serializer.data)
            
        #Delete 
        def delete(self,request,id ,format=None):
            users=self.get_object(id)
            users.delete() 
            logger.info("Record deleted successfully")
            return Response("Successfully_deleted")
