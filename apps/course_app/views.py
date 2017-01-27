from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
    'courses': Course.objects.all()
    }
    return render(request, 'course.html', context)

def course(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'],)

    return redirect('/')

def delete(request, id):
    delete_course = Course.objects.get(id=id)
    if request.method == "GET":
        return render(request, 'delete.html', { 'course' : delete_course })
    else:
        delete_course.delete()
        return redirect('/')
