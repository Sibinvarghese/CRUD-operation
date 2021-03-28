from django import forms
from .models import Employees
class EmployeeForm(forms.ModelForm): 
    class Meta:
        model=Employees
        fields=('fullname','phnumber','emp_code','position')
        labels={
            'fullname':'Full Name',
            'phnumber':'Mobile Number',
            'emp_code':'EMP.Code',
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields["position"].empty_label="Select"
        self.fields["emp_code"].required=False
