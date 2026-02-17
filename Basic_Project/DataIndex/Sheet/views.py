from django.shortcuts import render, HttpResponse
from .models import student

# Create your views here.
def show(request):
    list = student.objects.all().order_by('Serial')
    return render(request, "data.html", {"data":list})