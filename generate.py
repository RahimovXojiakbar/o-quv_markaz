import os
import django
import random
from faker import Faker

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from main.models import Student, Group, Teacher  # Import models after setup

# Initialize Faker
fake = Faker()

# Define choices
english_level = (
    ('STARTER', 'STARTER'),
    ('BEGINNER', 'BEGINNER'),
    ('PREINTERMEDIATE', 'PREINTERMEDIATE'),
    ('INTERMEDIATE', 'INTERMEDIATE'),
    ('UPPERINTERMEDIATE', 'UPPERINTERMEDIATE'),
    ('ADVANCED', 'ADVANCED'),
    ('IELTS', 'IELTS'),
)

group_status = (
    ('INPROGRESS', 'INPROGRESS'),
    ('COMPLETED', 'COMPLETED'),
    ('WAITING', 'WAITING'),
    ('CANCELED', 'CANCELED'),
)


teacher_level = ['IELT 8', 'IELT 7.5', 'IELT 7', 'IELT 6.5', "C1", 'C2']


# Clear existing data
Student.objects.all().delete()
Group.objects.all().delete()
Teacher.objects.all().delete()

# Create Students
students = []
for _ in range(100):
    student = Student(
        fullname=fake.name(),
        phone=fake.phone_number(),
        address=fake.address(),
        age=random.randint(18, 50)
    )
    student.save()
    students.append(student)

print('Successfully created 50 students.')

# Create Groups
groups = []
for _ in range(50):
    group = Group(
        title=fake.word().capitalize() + ' Group',
        level=random.choice([choice[0] for choice in english_level]),
        status=random.choice([choice[0] for choice in group_status]),
        description=fake.text(),
        price=round(random.uniform(100, 1000), 2)
    )
    group.save()
    # Add random students to the group
    group.students.add(*random.sample(students, k=random.randint(5, 15)))
    groups.append(group)

print('Successfully created 10 groups.')

# Create Teachers
for _ in range(100):
    teacher = Teacher(
        fullname=fake.name(),
        level=random.choice(teacher_level),
        about=fake.text(),
        hire_time=fake.date_time_this_decade()
    )
    teacher.save()
    # Add random groups to the teacher
    teacher.group.add(*random.sample(groups, k=random.randint(1, 3)))

print('Successfully created 5 teachers.')