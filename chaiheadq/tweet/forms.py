
from django import forms
from .models import Tweet



class TweetForm(forms.ModalForm):
    class Meta:
        modal = Tweet 
        fields = ['text', 'photo']
