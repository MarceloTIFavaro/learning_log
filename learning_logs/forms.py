from django import forms 
from .models import Topic 

class TopicForm(froms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        label = {''}