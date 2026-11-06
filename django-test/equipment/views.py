from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from .models import Equipment

def home(request):
    items = Equipment.objects.all().order_by("name")
    return render(request, "equipment/home.html",
                  {"items": items})
