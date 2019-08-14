from django.http import HttpResponse


def index(request):
    return HttpResponse("Congratulations you launched a Django application")
