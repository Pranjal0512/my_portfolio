from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    views={}
    views['services']= Service.objects.all()
    views['contacts']= Contact.objects.all()
    views['testimonials']= Testimonial.objects.all()
    views['design_skills']= Design_Skill.objects.all()
    views['coding_skills']= Coding_Skill.objects.all()
    views['educations']= Education.objects.all()
    views['experiences']= Experience.objects.all()
    views['informations']= Information.objects.all()
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        data = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        data.save()

    return render(request,'index.html',views)


