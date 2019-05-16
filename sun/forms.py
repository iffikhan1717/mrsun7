from django.forms import ModelForm
from .models import Employees, Accounts, Parts, ManiPro,EmpAccounts
from django import forms

class PartsForm(forms.ModelForm):

    class Meta:
        model = Parts
        fields = ['name', 'qty']


class ManiProForm(forms.ModelForm):
    class Meta:
        model = ManiPro
        fields = ['name','qty','dat']


class AccountsForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = ['accounts_name', 'credit', 'debit', 'opn_date']
#
#
class EmpAccForm(forms.ModelForm):
    class Meta:
        model = EmpAccounts
        fields = ['emp_account_name', 'emp_accounts_credit', 'emp_accounts_debit','dat','employees_employees']



class EmployeeForm(ModelForm):
    class Meta:
        model = Employees
        fields = ['employees_name', 'employees_job_title', 'employees_salary']




