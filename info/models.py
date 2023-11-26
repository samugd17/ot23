from django.db import models

class Competitor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=60, blank=True)
    birthdate = models.DateField(auto_now=False)
    # subject
    city = models.CharField(max_length=30)
    # job
    hobbies = models.TextField()
    avatar = models.ImageField(upload_to='competitors/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=60, blank=True)
    #subject
    avatar = models.ImageField(upload_to='teachers/%Y/%m/%d/', blank=True)

class Judge(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=60, blank=True)
    #job
    avatar = models.ImageField(upload_to='judges/%Y/%m/%d/', blank=True)    
