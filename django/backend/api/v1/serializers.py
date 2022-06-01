from rest_framework import serializers
from student.models import Student,School

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('firstname','lastname','school')

class schoolserializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields=('__all__')

