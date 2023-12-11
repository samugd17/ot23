import os
import sys

from django import setup
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ot.settings")
sys.path.append(settings.BASE_DIR)
setup()

from django.core.files import File
from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404
from PIL import Image

from info.models import Competitor, Judge, MusicStyle, Teacher

# Equivalencias
#  CSV -> txt
#   _  ->  ,
#   -  -> " "


def reset_database_objects():
    Competitor.objects.all().delete()
    Judge.objects.all().delete()
    Teacher.objects.all().delete()
    MusicStyle.objects.all().delete()


# Creacion de jueces
def create_judges():
    with open("judges_data.csv", "r") as f:
        fields = f.readline()
        judges = f.readlines()
        for judge in judges:
            judge = judge.split(",")
            first_name = judge[0]
            last_name = judge[1]
            slug = (
                "-".join([first_name, last_name])
                .lower()
                .replace('á', 'a')
                .replace('é', 'e')
                .replace('í', 'i')
                .replace('ó', 'o')
                .replace('ú', 'u')
            )
            job = judge[2].replace("_", ", ").replace("-", " ").capitalize()
            try:
                judge = Judge.objects.get(slug=slug)
                continue
            except Judge.DoesNotExist:
                new_judge = Judge.objects.create(
                    first_name=first_name, last_name=last_name, slug=slug, job=job
                )
                judge_picture_file_name = f"{new_judge.first_name.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')}.jpg"
                # Get participant picture url
                img_file_url = f"{settings.MEDIA_ROOT}/judges/{judge_picture_file_name}"
                # Associate participant picture with participant avatar
                #with open(img_file_url, "rb") as judge_picture:
                #    os.remove(img_file_url)
                #    new_judge.avatar.save(judge_picture_file_name, judge_picture, save=True)


# Creacion de profesores
def create_professors():
    with open("professors_data.csv", "r") as f:
        fields = f.readline()
        professors = f.readlines()
        for professor in professors:
            professor = professor.split(",")
            first_name = professor[0]
            last_name = professor[1]
            slug = (
                "-".join([first_name, last_name])
                .lower()
                .replace('á', 'a')
                .replace('é', 'e')
                .replace('í', 'i')
                .replace('ó', 'o')
                .replace('ú', 'u')
            )
            subject = professor[2].replace("_", ", ").replace("-", " ").capitalize()
            try:
                professor = Teacher.objects.get(slug=slug)
                continue
            except Teacher.DoesNotExist:
                new_professor = Teacher.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    slug=slug,
                    subject=subject,
                )
                professor_picture_file_name = f"{new_professor.first_name.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')}.jpg"
                # Get participant picture url
                img_file_url = f"{settings.MEDIA_ROOT}/professors/{professor_picture_file_name}"
                # Associate participant picture with participant avatar
                #with open(img_file_url, "rb") as professor_picture:
                #    os.remove(img_file_url)
                #    new_professor.avatar.save(
                #        professor_picture_file_name, professor_picture, save=True
                #    )


# Creacion de participantes
def create_participants():
    with open("participants_data.csv", "r") as f:
        # Dispatch first line (fields line)
        fields = f.readline()
        # Get all participants
        participants = f.readlines()
        for participant in participants:
            # Get data from each participant in each iteration
            participant = participant.split(",")
            first_name = participant[0]
            last_name = participant[1]
            slug = (
                "-".join([first_name, last_name])
                .lower()
                .replace('á', 'a')
                .replace('é', 'e')
                .replace('í', 'i')
                .replace('ó', 'o')
                .replace('ú', 'u')
                .replace("ñ", "n")
            )
            birthdate = "-".join(participant[2].split("/")[::-1])
            city = participant[3].replace("-", " ")
            job = participant[4].replace("_", ", ").replace("-", " ").capitalize()
            hobbies = participant[5].replace("_", ", ").replace("-", " ").capitalize()
            participant_music_styles = participant[6].replace("-", " ").strip().lower().split("_")
            # Create participant object
            try:
                participant = Competitor.objects.get(slug=slug)
                continue
            except Competitor.DoesNotExist:
                new_participant = Competitor(
                    first_name=first_name,
                    last_name=last_name,
                    slug=slug,
                    birthdate=birthdate,
                    city=city,
                    job=job,
                    hobbies=hobbies,
                )
                # Create music style objects, if it exist, get it
                music_styles = []
                for participant_music_style in participant_music_styles:
                    participant_music_style = participant_music_style.title()
                    try:
                        music_style = MusicStyle.objects.create(
                            name=participant_music_style, slug=participant_music_style.lower()
                        )
                    except IntegrityError:
                        music_style = MusicStyle.objects.get(name=participant_music_style)
                    music_styles.append(music_style)
                new_participant.save()
                new_participant.style.add(*music_styles)
                # Get participant picture name
                participant_picture_file_name = f"{new_participant.first_name.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')}.jpg"
                # Get participant picture url
                img_file_url = f"{settings.MEDIA_ROOT}/participants/{participant_picture_file_name}"
                # Associate participant picture with participant avatar
                #with open(img_file_url, "rb") as participant_picture:
                #    os.remove(img_file_url)
                #    new_participant.avatar.save(
                #        participant_picture_file_name, participant_picture, save=True
                #    )


reset_database_objects()
create_participants()
create_judges()
create_professors()
