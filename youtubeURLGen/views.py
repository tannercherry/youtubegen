from django.shortcuts import render
from youtubegen.forms import urlForm
from .models import urlInput

def input(request):
    form = urlForm(request.POST)
    if request.method == "POST" and form.is_valid():
            web_url = form.cleaned_data['web_url']
            web_url2 = web_url.replace("https://www.youtube.com/watch?v=", "")
            form.web_url = web_url2
            form.save()

    return render(request, 'urlInput/index.html', {'form': form})

def urls(request):
    urlAddresses = urlInput.objects.all().values_list()
    return render(request, 'urlInput/urls.html', {'urlAddresses' : urlAddresses})