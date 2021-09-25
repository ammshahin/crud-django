from django.forms import fields

from employee_reg.models import Employee
from django import forms
from . import models

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fullName','mobileNo','emp_code','position')
        labels = {
            'fullName' : 'Name',
            'mobileNo' : 'Telephone',
            'emp_code':'Employee Code',
            'position': 'Designation'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False