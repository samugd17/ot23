from django.db import models
from django.urls import reverse


class MusicStyle(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=30, blank=True, unique=True)

    def __str__(self):
        return self.name


class Competitor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    slug = models.SlugField(max_length=70, blank=True)
    birthdate = models.DateField(auto_now=False)
    city = models.CharField(max_length=40)
    job = models.CharField(max_length=120)
    hobbies = models.TextField(blank=True)
    favourite_singer_song = models.TextField(blank=True)
    curious_data = models.TextField(blank=True)
    style = models.ManyToManyField(MusicStyle)
    avatar = models.ImageField(upload_to='competitors/%Y/%m/%d/', blank=True)

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("info:competitor_detail", kwargs={"slug": self.slug})


class Teacher(models.Model):
    class Subjects(models.TextChoices):
        REVIEW = "REW", "Repaso"
        CHOREOGRAPHY = "CHP", "Coreografía"
        FITNESS = "FIT", "Fitness"
        YOGA = "YOG", "Yoga"
        MUSICAL_DIRECTOR = "MDR", "Dirección Musical"
        VOCAL_TECHNIQUE = "VTC", "Técnica Vocal"
        URBAN_DANCE = "UDC", "Baile Urbano"
        ENGLISH = "ENG", "Inglés"
        CHORAL_SINGING = "CSG", "Canto Coral"
        INTERPRETATION = "INT", "Interpretación"

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=60, blank=True)
    subject = models.CharField(max_length=3, choices=Subjects.choices, null=True)
    avatar = models.ImageField(upload_to='teachers/%Y/%m/%d/', blank=True)

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("info:teacher_detail", kwargs={"slug": self.slug})


class Judge(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=60, blank=True)
    job = models.CharField(max_length=120)
    avatar = models.ImageField(upload_to='judge/%Y/%m/%d/', blank=True)

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("info:judge_detail", kwargs={"slug": self.slug})
