from django.shortcuts import render,get_object_or_404
from .models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.parsers import JSONParser,FormParser,MultiPartParser

# Create your views here.

def addStudent(request):
    return render(request,'student/add.html')


class studentView(APIView):
    #parser_classes = (FormParser, JSONParser, MultiPartParser)

    def get(self,request):
        #stud=get_object_or_404(student)
        stud=student.objects.all()
        ser = studentSerializer(stud,many=True)
        return Response(ser.data)
        #return Response({'message':'Fail to Retrive data'})

    def post(self,request):
        ser=studentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'message':'Data Save succesfully...'})
        return Response({'message': 'Data Not Saves...'})
