from django.forms import forms, CharField, TextInput


class LostDocumentForm(forms.Form):
    document = CharField(max_length=100, widget=TextInput(attrs={"class": "form-control"}))
