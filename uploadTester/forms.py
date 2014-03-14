from django import forms


class UploadForm(forms.Form):
    time = forms.HiddenInput()
