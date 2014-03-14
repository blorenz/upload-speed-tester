from django.shortcuts import render, redirect, HttpResponse
from .forms import UploadForm
from django.views.decorators.csrf import csrf_exempt

def home(request):
    time_took = None
    if request.POST:
        form = UploadForm(request.POST)
        if form.is_valid():
            time_took = form.cleaned_data['time']
    else:
        form = UploadForm()

    return render(request, "welcome.html", { "form": form, "time_took": time_took})


import json

@csrf_exempt
def videopost(request):
    serialized = {"coolness":"idone"}
    if request.POST:
        serialized = {"coolness":"done"}

    return HttpResponse(json.dumps(serialized), mimetype="application/json")