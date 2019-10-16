from django.shortcuts import render, redirect, get_object_or_404
from exams.models import Exam
from exams import forms


def home_page_view(request):
	return render(request, 'home.html')


def create_exam_view(request):
    form = forms.NewExamForm()
    return render(request, 'create_exam.html', context={'form': form})
