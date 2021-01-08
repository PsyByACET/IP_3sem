from .models import task
from django import forms
from django.forms import ModelForm, Textarea, TextInput, DateInput, CheckboxInput, Select

class DateInput(forms.DateInput):
    input_type = 'date'

class taskForm(ModelForm):
    class Meta:
        model = task
        fields = ['title', 'task', 'task_date', 'status', 'user_id']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название задачи'
            }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст задачи'
            }),
            'task_date': DateInput( attrs={
                'class': 'form-control',

            }),
            'status': CheckboxInput(attrs={
                'class': 'form-control',

            }),
            'user_id': Select(attrs={
                'class': 'form-control',

            }),
            
        }

        