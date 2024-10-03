from django.shortcuts import render,get_object_or_404,redirect
from . import models
from . import forms
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
def homepage(request):
    company = models.Company.objects.all()
    return render(request,'home.html',{'companys':company})


def registration(request):
    if request.method =='POST':
        form  = forms.RegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form  = forms.RegForm()
    return render(request,'signup.html',{'form':form})



def sign_in(request):
    if request.method =='POST':
        form  = forms.LoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form  = forms.LoginForm()
    return render(request,'login.html',{'form':form})

def log_out(request):
    logout(request)
    return redirect('home')



def course_detail(request, id):
    course = get_object_or_404(models.Course, id=id)
    return render(request, 'course_detail.html', {'course': course})


def detail(request,id):
    company = get_object_or_404(models.Company,id=id)
    comments = models.Comments.objects.filter(company_id=id)
    if request.method=='POST':
        comment_form = forms.commentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.company_id = company
            new_comment.username = request.user
            new_comment.save()
            return redirect('detail',id=company.id)
    else :
            comment_form = forms.commentForm()
    return render(request,'detail.html',{'company':company,'comments':comments,'comment_form':comment_form})

@login_required

def update_post(request,id):
    company_post=get_object_or_404(models.Company,id=id)
    if company_post.author!=request.user:
        return redirect('home')
    model = models.Company.objects.get(id=id)
    form = forms.CompanyForm(request.POST or None,request.FILES,instance=model)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'update_post.html',{'form':form , 'model':model})

@login_required
def delete_post(request,id):
    company_post = get_object_or_404(models.Company,id=id)
    if company_post.author!=request.user:
        return redirect('home')
    model = models.Company.objects.get(id=id)
    form = forms.CompanyForm(request.POST or None,request.FILES,instance=model)
    if request.method=='POST':
        model.delete()
        return redirect('home')
    return render(request,'delete.html',{'form':form})

