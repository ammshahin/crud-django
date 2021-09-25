from employee_reg.forms import EmployeeForm
from django.http import request
from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import Employee

def employee_list(request):
    context = {'employee_list' : Employee.objects.all()}
    return render(request,'employee_reg/employee_list.html',context)

def employee_form(request):
    if request.method == "GET":
        form = EmployeeForm()
        return render(request,'employee_reg/employee_form.html',{'form':form})
    else:
        form = EmployeeForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')
    

def employee_delete (request):
    return render(request,'employee_reg/employee_delete.html')