from rest_framework.serializers import ModelSerializer,SlugRelatedField
from usercrud.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','contact']