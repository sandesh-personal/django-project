from django.contrib import admin
from .models import Student, Classroom, Teachers # * to import all models from modesl.py
# Register your models here.

admin.site.register(Classroom)
admin.site.register(Student)
admin.site.register(Teachers)