from django.shortcuts import HttpResponse

def sayHello(request, name):
    html="<h1>Hello, {}!</h1>".format(name)
    return HttpResponse()