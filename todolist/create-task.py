from asyncio import Task
from django import forms

class CreateTaskForm(forms.Form):
    class Meta:
        model_task = Task
        task_fields = ['display_task']
        desc_fields = ['display_desc']
    error_messages = {
        'required' : 'Please Type'
    }

    input_attrs = {
        'type' : 'text',
        'placeholder' : 'Task'
    }

    display_task = forms.CharField(label='', required=False,
        widget=forms.TextInput(attrs=input_attrs))

    display_desc = forms.CharField(label='', required=False,
        widget=forms.TextInput(attrs=input_attrs))