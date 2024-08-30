from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import Group
from users.models import User

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        # Create user
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data.get('name')
        )
        return user

    def validate_password(self, value):
        # Ensure password is provided and has some length
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'name', 'email', 'password']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }  # Options for each property, if we want to return on save or no
#
#     # Override method create so we can hash the password
#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)  # Seting password
#         instance.save()
#         return instance
