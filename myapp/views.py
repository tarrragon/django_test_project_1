from django.shortcuts import render


from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World!")
def index(request):
    return HttpResponse("Hello, world. You're at the myapp index.")