from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def login(req):
    return render_to_response('login.html')

@csrf_exempt
def authentication(req):
    print(req.POST)
    return HttpResponse('successfullly rendered')