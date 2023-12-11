from django.shortcuts import get_object_or_404, render

from .models import Competitor, Judge, Teacher


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'info/teacher/list.html', {'teachers': teachers})


def teacher_detail(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    return render(request, 'info/teacher/detail.html', {'teacher': teacher})


def judge_list(request):
    judges = Judge.objects.all()
    return render(request, 'info/judge/list.html', {'judges': judges})


def judge_detail(request, slug):
    judge = get_object_or_404(Judge, slug=slug)
    return render(request, 'info/judge/detail.html', {'judge': judge})


def competitor_list(request):
    competitors = Competitor.objects.all()
    return render(request, 'info/competitor/list.html', {'competitors': competitors})


def competitor_detail(request, slug):
    competitor = get_object_or_404(Competitor, slug=slug)
    return render(request, 'info/competitor/detail.html', {'competitor': competitor})


def homepage(request):
    return render(request, 'homepage.html')
