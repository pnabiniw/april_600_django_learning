from rest_framework.views import APIView
from rest_framework.response import Response
from crud.models import Student, ClassRoom


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
            return Response({"detail": "Not Found"})
        return Response({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "address": student.address
        })


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
        })


class ClassRoomView(APIView):
    def get(self, *args, **kwargs):
        classrooms = ClassRoom.objects.all()
        response = []
        for classroom in classrooms:
            response.append({
                "id": classroom.id,
                "name": classroom.name
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
        })
