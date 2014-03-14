from django import forms


class UploadForm(forms.Form):
    time = forms.CharField(max_length=20)
