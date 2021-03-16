import socket

from django.http import HttpResponse


def index(request):
    return HttpResponse(
        f"Congratulations you launched a Django application {socket.gethostname()}."
    )
