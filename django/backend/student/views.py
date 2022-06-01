from rest_framework import viewsets, mixins
from .models import Student,School
from api.v1.serializers import studentserializer,schoolserializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = studentserializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = schoolserializer
