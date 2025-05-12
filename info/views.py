from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .forms import SearchForm
from .models import Competitor, Judge, Teacher, MusicStyle


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'info/teacher/list.html', dict(teachers=teachers, section='Profesores'))


def teacher_detail(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    return render(request, 'info/teacher/detail.html', dict(teacher=teacher, section='Profesores'))


def judge_list(request):
    judges = Judge.objects.all()
    return render(request, 'info/judge/list.html', dict(judges=judges, section='Jurado'))


def judge_detail(request, slug):
    judge = get_object_or_404(Judge, slug=slug)
    return render(request, 'info/judge/detail.html', dict(judge=judge, section='Jurado'))


def competitor_list(request):
    competitors = Competitor.objects.all()
    return render(
        request, 'info/competitor/list.html', dict(competitors=competitors, section='Alumnos')
    )


def competitor_detail(request, slug):
    competitor = get_object_or_404(Competitor, slug=slug)
    music_styles = MusicStyle.objects.filter(competitor=competitor)
    return render(
        request,
        'info/competitor/detail.html',
        dict(competitor=competitor, music_styles=music_styles, section='Alumnos'),
    )


def homepage(request):
    return render(request, 'info/homepage.html')


def search(request):
    form = SearchForm(request.GET)
    competitor_results = []
    teacher_results = []
    judge_results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        competitor_results = Competitor.objects.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(city__icontains=query)
            | Q(style__name__icontains=query)
        ).distinct()

        judge_results = Judge.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        ).distinct()

        teacher_results = Teacher.objects.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(subject__icontains=query)
        ).distinct()

    return render(
        request,
        'results.html',
        {
            'form': form,
            'competitor_results': competitor_results,
            'teacher_results': teacher_results,
            'judge_results': judge_results,
        },
    )
