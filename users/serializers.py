from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
            "full_name",
            "artistic_name",
        ]
        read_only_fields = ["id"]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"validators": [UniqueValidator(User.objects.all())]},
        }

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()
        return instance
