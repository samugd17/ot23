from django.urls import path

from . import views

app_name = 'info'

urlpatterns = [
    path("teachers/", views.teacher_list, name="teacher_list"),
    path("teachers/<slug:slug>", views.teacher_detail, name="teacher_detail"),
    path("judge/", views.judge_list, name="judge_list"),
    path("judge/<slug:slug>", views.judge_detail, name="judge_detail"),
    path("competitors/", views.competitor_list, name="competitor_list"),
    path("competitors/<slug:slug>", views.competitor_detail, name="competitor_detail"),
]
