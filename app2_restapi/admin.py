from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['emp_id', 'first_name', 'last_name', 'age', 'phone_number', 'salary', 'city']

admin.site.register(Employee, EmployeeAdmin)
