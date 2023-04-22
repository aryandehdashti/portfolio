from django.db import models

# Create your models here.

class MyInfo(models.Model):
    fullName = models.CharField(max_length=30)
    miniDescribe = models.CharField(blank=True, null=True, max_length=255)
    avatar = models.ImageField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True, max_length=20)
    email = models.EmailField(blank=True, null=True, max_length=255)
    cv = models.FileField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.fullName
    

class About(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    describe1 = models.TextField(blank=True, null=True)
    describe2 = models.TextField(blank=True, null=True)
    aboutAvatar = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=230, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    
class Skill(models.Model):
    title = models.CharField(max_length=50)
    grade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
    