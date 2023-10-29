from django import forms
from .models import Announcement

class AnnouncementAddForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'description', 'cost', 'location']

    title = forms.CharField(widget=forms.TextInput(attrs={"class":"stylforma"}), max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={"class":"stylforma"}), required=True)
    cost = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"stylforma"}),required=True)
    location = forms.CharField(widget=forms.TextInput(attrs={"class":"stylforma"}), max_length=100, required=True)
    
