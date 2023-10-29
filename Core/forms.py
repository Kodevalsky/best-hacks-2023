from django import forms
from Offer.models import Announcement

class AnnouncementForm(forms.ModelForm):
    title = forms.CharField(
        required=False,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Czego szukasz?",
                "class": "column is-one-third",
            }
        ),
        label="",
    )
    location = forms.CharField(
        required=False,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Miasto",
                "class": "column is-one-third",
            }
        ),
        label="",
    )

    class Meta:
        model = Announcement
        exclude = ("id", "description", "username", "cost", "created_at", "promoted", )
