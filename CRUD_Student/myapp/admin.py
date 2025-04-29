from django.contrib import admin
from myapp.models import StudentModel
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone','password']
    
admin.site.register(StudentModel, StudentAdmin)