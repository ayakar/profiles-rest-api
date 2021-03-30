from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model=models.UserProfile
        fields=('id','email','name','password')
        extra_kwargs={
            'password':{
                'write_only': True,
                'style':{
                    'input_type':'password'
                }
            }
        }

    #overwrite default create function which create a new object in db
    def create(self, validated_data):
        """Create and return a new user"""
        user =models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            #replacing passward
            password = validated_data.pop('password')
            #hashing
            instance.set_password(password)

        # passing the values to the existing DRF update() method, to handle updating the remaining fields
        return super().update(instance, validated_data)


