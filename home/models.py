from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=300)
    logo = models.CharField(max_length=300)
    description = models.TextField()
    # money = models.IntegerField()

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    image = models.TextField()
    name = models.CharField(max_length=300)
    post = models.CharField(max_length=300)
    description = models.TextField()


    def __str__(self):
        return self.name


class Design_Skill(models.Model):
    name=models.CharField(max_length=300)
    level=models.IntegerField()
    color=models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Coding_Skill(models.Model):
    name=models.CharField(max_length=300)
    level=models.IntegerField()
    color=models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Education(models.Model):
    name=models.CharField(max_length=300)
    starting_year=models.IntegerField()
    ending_year=models.IntegerField()
    university=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Experience(models.Model):
    name=models.CharField(max_length=300)
    starting_year=models.IntegerField()
    ending_year=models.IntegerField()
    university=models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Information(models.Model):
    address= models.CharField(max_length=400)
    phone= models.IntegerField()
    email= models.EmailField(max_length=300)
    def __str__(self):
        return self.address


INDEX = (('first','first'),('second','second'),('third','third'),('fourth','fourth'))
class Project(models.Model):
    slug = models.CharField(max_length=500, unique=True)
    item_no = models.CharField( choices= INDEX, max_length=300)
    image = models.ImageField(upload_to='img')
    drive= models.TextField()

    def __str__(self):
        return self.slug






