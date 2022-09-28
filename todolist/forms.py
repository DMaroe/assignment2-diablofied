from django.forms import ModelForm
from todolist.models import Tasks

class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description']