from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import response, status
from rest_framework.views import APIView
from rest_framework.response import Response

class EmployeeList(APIView):
    def get(self, request):
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

    def post(self):
        pass
        
