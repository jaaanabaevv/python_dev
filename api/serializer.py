from lear_code.models import Company,Course,Mentor
from rest_framework.serializers import ModelSerializer

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CoursesSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class MentorSerializer(ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'

