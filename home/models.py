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
    Post = models.CharField(max_length=300)
    Description = models.TextField()


    def __str__(self):
        return self.name


class Skill(models.Model):
    name=models.CharField(max_length=300)
    level=models.IntegerField()

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
    email= models.EmailField(max_length=15)
    def __str__(self):
        return self.address




