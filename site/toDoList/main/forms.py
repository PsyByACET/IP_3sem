from .models import task
from django import forms
from django.forms import ModelForm, Textarea, TextInput, DateInput, CheckboxInput, Select, NumberInput

class DateInput(forms.DateInput):
    input_type = 'date'

class pointsFilterForm(forms.Form):
    min_points = forms.IntegerField(label="От", required=False)
    max_points = forms.IntegerField(label="До", required=False)

class taskForm(ModelForm):
    class Meta:
        model = task
        fields = ['title', 'task', 'task_date', 'status', 'user_id']
        widgets = {
            'title': TextInput(attrs={
                'id': 'title',
                'class': 'form-control',
                'placeholder': 'Название задачи'
            }),
            'task': Textarea(attrs={
                'id': 'task',
                'class': 'form-control',
                'placeholder': 'Текст задачи'
            }),
            'task_date': DateInput( attrs={
                'id': 'task_date',
                'class': 'form-control',

            }),
            'status': CheckboxInput(attrs={
                'id': 'status',
                'class': 'form-control',

            }),
            
            'user_id': Select(attrs={
                'id': 'user_id ',
                'class': 'form-control',

            }),
            
        }

        