from django.shortcuts import render
from student.models import student
from rest_framework.response import Response
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser

from django.http import JsonResponse,HttpResponse
from rest_framework.views import APIView
from .serializers import studentSerializer

# Create your views here.

def homeView(request):
    return render(request,'Home.html')

def registerView(request):
    serializer=studentSerializer
    return render(request,'register.html',{'serializer':serializer})

def showView(request):
    return render(request,'show.html')



class register(APIView):
    parser_classes = (FormParser,JSONParser, MultiPartParser)


    def get(self,request,pk=0):
        if pk==0:
            stud=student.objects.all()
            ser = studentSerializer(stud, many=True)
        else:
            stud=student.objects.get(pk=pk)
            ser = studentSerializer(stud)


        return Response(ser.data)

    def post(self,request,pk=0):
        ser=studentSerializer(data=request.data)

        if ser.is_valid():
            ser.save()
            return JsonResponse({"message":"Data Save Succesfully"})
        return JsonResponse({"message": "Data Not Save "})


    def delete(self,request,pk):

        stud = student.objects.get(pk=pk)
        ser = studentSerializer(stud)
        #stud.delete()
        return JsonResponse({'message':'Record Deleted Succesfully'})

    def put(self,request,pk):
        stud = student.objects.get(pk=pk)
        ser = studentSerializer(stud,data=request.data)
        if ser.is_valid():
            ser.save()
            return JsonResponse({'message':'Record Update Succesfully'})
        return JsonResponse({'message': 'Some Problem is Occure'})