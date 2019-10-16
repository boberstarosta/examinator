from django import forms
from exams.models import Exam


class NewExamForm(forms.ModelForm):

    class Meta:
        model = Exam
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control input-lg'
            })
        }
