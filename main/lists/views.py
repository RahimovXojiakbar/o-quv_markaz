from django.shortcuts import render
from main import models

def index(request):
    teachers = models.Teacher.objects.all().order_by('fullname')
    groups  = models.Group.objects.filter(status = 'WAITING')
    context = {
        'teachers': teachers,
        'groups': groups
        
    }
    return render(request, 'index.html', context)