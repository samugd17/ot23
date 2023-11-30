from django.db import models


class MusicStyle(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=30, blank=True)

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

    def __str__(self):
        return self.first_name


class Teacher(models.Model):
    class Subjects(models.TextChoices):
        REVIEW = "REW", "Review"
        CHOREOGRAPHY = "CHP", "Choreography"
        FITNESS = "FIT", "Fitness"
        YOGA = "YOG", "Yoga"
        MUSICAL_DIRECTOR = "MDR", "Musical Director"
        VOCAL_TECHNIQUE = "VTC", "Vocal technique"
        URBAN_DANCE = "UDC", "Urban Dance"
        ENGLISH = "ENG", "English"
        CHORAL_SINGING = "CSG", "Choral Singing"
        INTERPRETATION = "INT", "Interpretation"

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=60, blank=True)
    subject = models.CharField(max_length=3, choices=Subjects.choices, null=True)
    avatar = models.ImageField(upload_to='teachers/%Y/%m/%d/', blank=True)


class Judge(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=60, blank=True)
    job = models.CharField(max_length=120)
    avatar = models.ImageField(upload_to='judge/%Y/%m/%d/', blank=True)
