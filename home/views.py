from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    views={}
    views['services']= Service.objects.all()
    views['contacts']= Contact.objects.all()
    views['testimonials']= Testimonial.objects.all()
    views['skills']= Skill.objects.all()
    views['educations']= Education.objects.all()
    views['experiences']= Experience.objects.all()
    views['informations']= Information.objects.all()
    return render(request,'index.html',views)


