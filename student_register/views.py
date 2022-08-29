from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def student_list(request):
    context = {
        'student_list' : Student.objects.all()
    }
    return render(request, "student_register/student_list.html", context)