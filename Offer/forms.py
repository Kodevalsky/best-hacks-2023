from django import forms
from .models import Announcement

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'description', 'cost', 'location']

    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    date = forms.DateField(widget=forms.SelectDateWidget, required=True)
    cost = forms.IntegerField(widget=forms.NumberInput,required=True)
    
