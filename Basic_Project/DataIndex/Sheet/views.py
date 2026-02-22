from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import student
from .forms import StudentForm

# Create your views here.
def show(request):
    list = student.objects.all().order_by('Serial')
    return render(request, "data.html", {"data":list})

def submission(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student record created successfully.")
            return redirect('StudentList')
        # if invalid, fall through to re‑render with errors
    else:
        form = StudentForm()
    return render(request, "submission.html", {"form": form})