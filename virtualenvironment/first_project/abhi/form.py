from django import forms  
from abhi.models import *
  
class EmpForm(forms.ModelForm):  
    class Meta:  
        model = employee1 
        fields = "__all__"  

class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 100)
    mobile = forms.IntegerField(label="enter mobile number")
    date = forms.DateTimeField(label="enter bdyr")
    file =forms.FileField()

