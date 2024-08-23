

from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        students = students.filter(student_name__icontains=search_query)

    filter_option = request.GET.get('filter', 'all')
    if filter_option == 'pass':
        students = students.filter(remarks='PASS')
    elif filter_option == 'fail':
        students = students.filter(remarks='FAIL')

    return render(request, 'student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})




