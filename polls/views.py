from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world. Inside Polls index')