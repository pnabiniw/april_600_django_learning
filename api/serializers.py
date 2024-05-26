from rest_framework import serializers
from django.contrib.auth.models import User
from crud.models import Student, ClassRoom


class ClassRoomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    email = serializers.EmailField()
    address = serializers.CharField(max_length=50)


class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ["id", "name"]


class StudentModelSerializer(serializers.ModelSerializer):
    # classroom = ClassRoomModelSerializer()

    class Meta:
        model = Student
        fields = ["id", "name", "age", "email", "address", "classroom"]

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method == "GET":
            fields["classroom"] = ClassRoomModelSerializer()
        return fields


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        password = validated_data["password"]
        user.set_password(password)
        user.save()
        return user
