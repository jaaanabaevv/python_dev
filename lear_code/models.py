from django.db import models
from django.contrib.auth.models import User


class Mentor(models.Model):
    full_name = models.CharField(max_length=255,verbose_name='mentordin F.I.O ')
    desc = models.TextField(verbose_name='mentor haqqinda')
    
    def __str__(self):
        return self.full_name

class Course(models.Model):
    title = models.CharField(max_length=255,verbose_name='kurs ati')
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='kurs baxasi')
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True, related_name='mentor')
    data = models.DateTimeField(verbose_name='kurs neshe ay dawam etedi')
    count_of_lessons = models.BigIntegerField(verbose_name='sabaxlar sani ')
    
    def __str__(self):
        return self.title

class Company(models.Model):
    title = models.CharField(max_length=255,verbose_name='company ati')
    desc = models.TextField(verbose_name='companiys haqqinda')
    courses = models.ManyToManyField(Course, related_name='companies')
    mentors = models.ManyToManyField(Mentor, related_name='companies')
    logo = models.ImageField(verbose_name='logo:',blank=True,null=True)
    pub_date = models.DateField()

    def __str__(self):
        return self.title

class Comments(models.Model):
    text = models.TextField(verbose_name='Komment text:')
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)