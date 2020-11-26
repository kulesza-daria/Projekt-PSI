from django.http import HttpResponse


def index(request):
    return HttpResponse("Hej To my :3")
