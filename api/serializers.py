from rest_framework import serializers
from crud.models import Student


class ClassRoomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    email = serializers.EmailField()
    address = serializers.CharField(max_length=50)


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "age", "email", "address", "classroom"]
