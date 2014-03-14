from django.shortcuts import render, redirect
from .forms import UploadForm
from django.views.decorators.csrf import csrf_exempt

def home(request):
    time_took = None
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        time_took = form.time
    else:
        form = UploadForm()

    return render(request, "welcome.html", { "form": form, "time_took": time_took})



@csrf_exempt
def videopost(request):
    return render(request, "welcome.html")