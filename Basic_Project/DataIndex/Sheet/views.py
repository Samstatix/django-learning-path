from django.shortcuts import render, HttpResponse, redirect
from .models import student

# Create your views here.
def show(request):
    list = student.objects.all().order_by('Serial')
    return render(request, "data.html", {"data":list})

def submission(request):
    if request.method == "POST":
        name = request.POST.get("name")
        serial = request.POST.get("serial")
        dob = request.POST.get("dob")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        student.objects.create(
            Name = name,
            Serial = serial,
            Birth_Date = dob,
            Email = email,
            Phone = phone,
            Address = address
        )
    return render(request, "submission.html")