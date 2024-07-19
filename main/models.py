from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

enlish_level = (
    ('STARTER', 'STARTER'),
    ('BEGINNER','BEGINNER'),
    ('PREINTERMEDIATE', 'PREINTERMEDIATE'),
    ('INTERMEDIATE','INTERMEDIATE'),
    ('UPPERINTERMEDIATE', 'UPPERINTERMEDIANTE'),
    ('ADVANCED','ADVANCED'),
    ('IELTS', 'IELTS'),
)

group_status = (
    ('INPROGRESS', 'INPROGRESS'),
    ('COMPLETED', 'COMPLETED'),
    ('WAITING', 'WAITING'),
    ('CANCELED', 'CANCELED'),
)

class Student(models.Model):
    fullname = models.CharField(max_length=230)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    
    def __str__(self) -> str:
        return self.fullname



class Group(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    level = models.CharField(choices=enlish_level, max_length=255, default='STARTER')
    status = models.CharField(max_length=255, choices=group_status, default='WAITING')
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    students  = models.ManyToManyField(Student, related_name='groups') 

    def __str__(self) -> str:
        return self.title + ' - ' + self.level




class Teacher(models.Model):
    img = models.ImageField(upload_to='Teacher_photo/', blank=True, null=True)
    fullname = models.CharField(max_length=50)
    level = models.CharField(max_length=240)
    about = CKEditor5Field()
    created = models.DateTimeField(auto_now_add=True)
    hire_time = models.DateTimeField()
    group = models.ManyToManyField(Group, related_name='teachers')

    def __str__(self) -> str:
        return self.fullname + ' - '+ self.level