from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.generics import ListAPIView,UpdateAPIView,CreateAPIView,RetrieveAPIView
from .serializer import CompanySerializer,MentorSerializer,CoursesSerializer
from lear_code.models import Company,Mentor,Course

class CompanyView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class=CompanySerializer

class UpdateCompanyView(UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer





class CreateCompanyView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class RetriveCompanyView(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    