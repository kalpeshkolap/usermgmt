from rest_framework.response import Response
from rest_framework.views import APIView
from usercrud.serializers import UserSerializer
from usercrud.models import User
# Create your views here.


class UserView(APIView):
    def get(self, request,format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    def post(self, request,format=None):
        name =request.data
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
