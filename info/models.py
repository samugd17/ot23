from django.db import models


class MusicStyle(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, blank=True)


class Competitor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=60, blank=True)
    birthdate = models.DateField(auto_now=False)
    city = models.CharField(max_length=30)
    job = models.CharField(max_length=30, blank=True)
    hobbies = models.TextField()
    style = models.ManyToManyField(MusicStyle)
    avatar = models.ImageField(upload_to='competitors/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


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
    subject = models.CharField(max_length=3, choices=Subjects.choices, default="")
    avatar = models.ImageField(upload_to='teachers/%Y/%m/%d/', blank=True)


class Judge(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=60, blank=True)
    job = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(upload_to='judge/%Y/%m/%d/', blank=True)
