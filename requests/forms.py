from django import forms
from django.forms import DateInput

from requests.models import Request


class RequestForm(forms.ModelForm):


    class Meta:
        model = Request
        # fields = "__all__"
        fields = ["email", "nickname", "volume", "description", "weight","place","send_date"]

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Описание",
                }
            ),
            "send_date": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),

        }


