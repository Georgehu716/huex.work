from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, this is huex.work</h1>")
