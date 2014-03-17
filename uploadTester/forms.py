from django import forms


class UploadForm(forms.Form):
    time = forms.CharField(max_length=20, widget=forms.HiddenInput())
    size = forms.CharField(max_length=20, widget=forms.HiddenInput())
