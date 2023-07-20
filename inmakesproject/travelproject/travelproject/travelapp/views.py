from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Actor



# Create your views here.
def demo(request):
    obj = Place.objects.all()
    objj=Actor.objects.all()
    return render(request, "index.html", {'result': obj,'result1':objj})
