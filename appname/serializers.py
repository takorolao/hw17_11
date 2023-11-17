from rest_framework.serializers import ModelSerializer
from .models import Course, Student

class StudentSelializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name' ,'email', 'username','password', 'phone', 'birthdate')

class ListStudentSelializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name' ,'email', 'phone')

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'price', 'description']
