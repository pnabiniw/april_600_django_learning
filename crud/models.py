from django.db import models


class ClassRoom(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Student(models.Model):  # default related name is "student_set" (modelname_set)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE,
                                  null=True, blank=True, related_name="students")
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"Student {self.name}"


class StudentProfile(models.Model):  # default related name is "studentprofile"
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14)
    bio = models.TextField(max_length=500)
    profile_picture = models.FileField(null=True, blank=True, upload_to="profile_pictures")

    def __str__(self):
        return f"Profile of {self.student.name}"

# class Question(models.Model):
#     question = CharField()
#     options = ArrayField()
#     answer = Charfield
#     active = Bool()
#     difficulty = PosInt()
#
# class Quiz(models.Model):
#     name = CharField()
#     questions = ManyToMany()
#
#
# class UserQuizAttempt():
#     quiz = Fk
#     question =
#     answer =
#     is_correct =
