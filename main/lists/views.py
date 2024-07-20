from django.shortcuts import render
from main import models
from django.core.paginator import Paginator

def paginate_queryset(queryset, items_per_page, page_number):
    paginator = Paginator(queryset, items_per_page)
    page_obj = paginator.get_page(page_number)
    return page_obj

def index(request):
    teachers = models.Teacher.objects.all().order_by('fullname')
    groups = models.Group.objects.filter(status='WAITING')

    page_number = request.GET.get('page', 1)
    
    teachers_page = paginate_queryset(teachers, 10, page_number)

    context = {
        'teachers': teachers_page,
        'groups': groups
    }
    return render(request, 'index.html', context)


def students(request):
    student = models.Student.objects.all().order_by('fullname')
    page_number = request.GET.get('page', 1)
    students_page = paginate_queryset(student, 30, page_number)

    context = {
        'students': students_page
    }
    return render(request, 'students.html', context)