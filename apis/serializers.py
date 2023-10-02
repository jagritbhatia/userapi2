from rest_framework import serializers
from .models import CustomUser

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True)
    class Meta:
        fields = (
                    "id",
                    "username",
                    "password",
                    "email",
        )
        model = CustomUser
        read_only_fields = ['id']
        
    
    def create(self, validated_data):
        # Hash the password before saving the user
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    

# class UserListSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#                     "id",
#                     "username",
#                     "email",
#         )
#         model = CustomUser