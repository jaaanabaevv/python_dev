from django.urls import path 
from .views import CompanyView,UpdateCompanyView,CreateCompanyView,RetriveCompanyView

urlpatterns = [
    path('',CompanyView.as_view(),name='home'),
    path('update/<int:id>',UpdateCompanyView.as_view()),
    path('create/',CreateCompanyView.as_view()),
    path('retrive/<int:pk>',RetriveCompanyView.as_view())
]