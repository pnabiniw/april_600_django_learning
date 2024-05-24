from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, UpdateAPIView, \
    RetrieveAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from crud.models import Student, ClassRoom
from .serializers import ClassRoomSerializer, \
    StudentSerializer, StudentModelSerializer, ClassRoomModelSerializer, UserModelSerializer
from .permissions import IsSuperAdminUser

# 1XX => Socket Communication
# 2XX => Success (200, 201, 204)
# 3XX => Redirection (301, 302)
# 4XX => Frontend Error (400, 401, 403, 404, 405)
# 5XX => Server Error (500, 502)

# class LoginRequiredMixin:
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

class StudentDetailView(APIView):
    def get(self, *args, **kwargs):  # (), {}
        # return Response({
        #     "id": 1,
        #     "name": "Jon",
        #     "age": 30,
        #     "address": "KTM"
        # })
        id = kwargs["id"]
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "address": student.address
        })

    def patch(self, request, *args, **kwargs):
        data = self.request.data
        if not data:
            return Response({
                "message": "Please mention name, age, email or address to update"
            })
        id = kwargs["id"]
        try:
            _ = Student.objects.get(id=id)
        except:
            return Response({
                "detail": "Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
        Student.objects.filter(id=id).update(**data)
        response = {"message": "Student updated successfully!"}
        response.update(data)
        return Response(response)


class StudentView(APIView):
    def get(self, *args, **kwargs):  # [{}, {}, {}]
        response = []
        students = Student.objects.all()
        for student in students:
            response.append({
                "id": student.id,
                "name": student.name,
                "age": student.age,
                "address": student.address
            })
        return Response(response)

    def post(self, *args, **kwargs):
        data = self.request.data
        if not data:
            return Response({"message": "name, age, email and address are required !"})
        if "name" not in data or "age" not in data or "email" not in data or "address" not in data:
            return Response({"message": "name, age, email and address are required !"})
        name = self.request.data["name"]
        age = self.request.data["age"]
        email = self.request.data["email"]
        address = self.request.data["address"]
        Student.objects.create(name=name, age=age, email=email, address=address)
        return Response({
            "message": "Student added successfully !",
            "name": name,
            "age": age,
            "email": email,
            "address": address
        }, status=status.HTTP_201_CREATED)


class ClassRoomView(APIView):
    def get(self, *args, **kwargs):
        classrooms = ClassRoom.objects.all()
        response = []
        for classroom in classrooms:
            response.append({
                "id": classroom.id,
                "name": classroom.name,

            })
        return Response(response)

    def post(self, *args, **kwargs):
        name = self.request.data.get("name")
        if not name:
            return Response({
                "name": "This field is required"
            })
        ClassRoom.objects.create(name=name)
        return Response({
            "message": "Classroom created successfully!",
            "name": name
        }, status=status.HTTP_201_CREATED)


    def patch(self, *args, **kwargs):
        data = self.request.data
        print(data)  # {"name": "Two", "age": 30, "email": "sdf"@sd.com}
        classroom_id = kwargs["id"]
        if not data or "name" not in data:
            return Response({
                "message": "name field is required for classroom update"
            }, status=status.HTTP_400_BAD_REQUEST)
        try:
            classroom = ClassRoom.objects.get(id=classroom_id)
        except ClassRoom.DoesNotExist:
            return Response({
                "detail": "Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
        ClassRoom.objects.filter(id=classroom.id).update(**data)  # (name="Two", age=30, email="sd@sd.com")
        classroom = ClassRoom.objects.get(id=classroom_id)
        return Response({
            "message": "Classroom updated successfully!",
            "id": classroom.id,
            "name": classroom.name
        })



class ClassRoomUsingSerializerDetailView(APIView):
    def get(self, *args, **kwargs):
        id = kwargs["id"]
        try:
            classroom = ClassRoom.objects.get(id=id)  # python_object
        except:
            return Response({
                "detail": "Not found"
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = ClassRoomSerializer(classroom)
        return Response(serializer.data)


class ClassRoomUsingSerializerView(APIView):

    """

        def get(self, *args, **kwargs):
            students = Student.objects.all()
            ser = StudentSerializer(students, many=True)
            return Response(ser.data)
    """
    def get(self, *args, **kwargs):
        classrooms = ClassRoom.objects.all()
        serializer = ClassRoomSerializer(classrooms, many=True) # Serialization
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        serializer = ClassRoomSerializer(data=self.request.data)  # deserialization
        if serializer.is_valid():
            validated_data = serializer.validated_data
            c = ClassRoom.objects.create(**validated_data)
            return Response({
                "message": "Classroom created successfully !",
                "id": c.id,
                "name": c.name
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Could not create class !",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class StudentUsingSerializerView(APIView):
    def get(self, *args, **kwargs):
        students = Student.objects.all()
        ser = StudentSerializer(students, many=True)
        return Response(ser.data)

    def post(self, *args, **kwargs):
        serializer = StudentSerializer(data=self.request.data)  # deserialization
        if serializer.is_valid():
            validated_data = serializer.validated_data
            s = Student.objects.create(**validated_data)
            return Response({
                "message": "Student created successfully !",
                "id": s.id,
                "name": s.name
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Could not create student !",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class StudentUsingModelSerView(APIView):
    def get(self, *args, **kwargs):
        students = Student.objects.all()
        ser = StudentModelSerializer(students, many=True, context={"request": self.request})
        return Response(ser.data)

    def post(self, *args, **kwargs):
        serializer = StudentModelSerializer(data=self.request.data, context={"request": self.request})  # deserialization
        if serializer.is_valid():
            s = serializer.save()
            return Response({
                "message": "Student created successfully !",
                "id": s.id,
                "name": s.name
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Could not create student !",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class ClassRoomGenericListView(ListAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomGenericCreateView(CreateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomGenericView(ListCreateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomGenericUpdateView(UpdateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomGenericDetailView(RetrieveAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomGenericDeleteView(DestroyAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class StudentUpdateRetrieveDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class ClassRoomViewSet(ModelViewSet):
    serializer_class = ClassRoomModelSerializer
    queryset = ClassRoom.objects.all()

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(), ]
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsSuperAdminUser(), ]
        if self.request.method == "POST":
            return [(IsAdminUser | IsSuperAdminUser)(), ]
        return [IsAuthenticated()]


class StudentViewSet(ModelViewSet):
    # permission_classes = [AllowAny]
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()


class UserViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
