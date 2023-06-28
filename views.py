from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
  
def reputation_tags(request):
    return render(request, 'reputation_tags.html')

def reputation_log(request):
    return render(request, 'reputation_log.html')
