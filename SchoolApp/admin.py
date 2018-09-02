from django.contrib import admin
from .models import student,subject,register,teacher,parent,department,course

# Register your models here.
admin.site.register(register)
admin.site.register(department)
admin.site.register(course)
admin.site.register(subject)
admin.site.register(parent)
admin.site.register(student)
admin.site.register(teacher)