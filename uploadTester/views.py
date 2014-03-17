from __future__ import division
from django.shortcuts import render, redirect, HttpResponse
from .forms import UploadForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

def humanize_bytes(bytes, precision=1):
    """Return a humanized string representation of a number of bytes.

    Assumes `from __future__ import division`.


    '1.3 GB'
    """
    abbrevs = (
        (1<<50L, 'PB'),
        (1<<40L, 'TB'),
        (1<<30L, 'GB'),
        (1<<20L, 'MB'),
        (1<<10L, 'kB'),
        (1, 'bytes')
    )
    if bytes == 1:
        return '1 byte'
    for factor, suffix in abbrevs:
        if bytes >= factor:
            break
    return '%.*f %s' % (precision, bytes / factor, suffix)

def home(request):
    form = UploadForm()
    return render(request, "welcome.html", { "form": form })


def form_submit(request):
    time_took = None
    size = None
    if request.POST:
        form = UploadForm(request.POST)
        if form.is_valid():
            time_took = form.cleaned_data['time']
            size = form.cleaned_data['size']
            size = humanize_bytes(long(size))
            messages.add_message(request, messages.INFO,'It took %s seconds to upload %s.' % (time_took, size) )
    return redirect('home')


import json

@csrf_exempt
def videopost(request):
    serialized = {"coolness":"idone"}
    if request.POST:
        serialized = {"coolness":"done"}

    return HttpResponse(json.dumps(serialized), mimetype="application/json")