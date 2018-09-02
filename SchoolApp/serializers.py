from rest_framework import serializers
from .models import *


class departmentSerializer(serializers.ModelSerializer):

    class Meta:
        model=department
        fields='__all__'



class courseSerializer(serializers.ModelSerializer):

    class Meta:
        model=course
        fields='__all__'


class subjectSerializer(serializers.ModelSerializer):

    class Meta:
        model=subject
        fields='__all__'



class parentSerializer(serializers.ModelSerializer):

    class Meta:
        model=parent
        fields='__all__'


class studentSerializer(serializers.ModelSerializer):

    class Meta:
        model=student
        fields='__all__'



class teacherSerializer(serializers.ModelSerializer):

    class Meta:
        model=teacher
        fields='__all__'
