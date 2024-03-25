from django.shortcuts import render, redirect
from .models import Course, Student
from .forms import CourseForm, StudentForm

def students(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()
    context = {'students': students, 'form': form, 'courses': courses}
    return render(request, 'students.html', context)

def courses(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm()
    context = {'courses': courses, 'form': form}
    return render(request, 'courses.html', context)

def details(request, student_id):
    student = Student.objects.get(pk=student_id)
    available_courses = Course.objects.exclude(students=student)  # Get non-registered courses
    if request.method == 'POST':
        selected_course = request.POST.get('courses')
        if selected_course:
            course = Course.objects.get(pk=selected_course)
            student.courses.add(course)
            return redirect('details', student_id=student.id)  # Redirect to updated student details
    context = {'student': student, 'available_courses': available_courses}
    return render(request, 'details.html', context)
