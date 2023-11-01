from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import *

class UserRegForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']

class DateInput(forms.DateInput):
    input_type='date'


class NoteDescForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['title','desc']




class HwForm(forms.ModelForm):
    class Meta:
        model=Homework
        widgets={'due':DateInput()}
        fields=['subject','title','desc','due','is_finished']



class DashboardForm(forms.Form):
    text=forms.CharField(max_length=100,label="Enter To Search ")



class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title','desc','is_finished']


class ConversationForm(forms.Form):
    # works like a calculator
    CHOICES=[('length','Length'),('mass','Mass')]
    measurement=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)



class MassConversion(forms.Form):
    # works like a calculator
    CHOICES=[('pound','Pound'),('kg','Kg')]
    input=forms.CharField(required=False,label=False,widget=forms.TextInput(attrs={'type':'number','placeholder':"Enter the Number"} ))
    measure1=forms.CharField(label='',widget=forms.Select(choices=CHOICES))

    measure2=forms.CharField(label='',widget=forms.Select(choices=CHOICES))


class LengthConversion(forms.Form):
    CHOICES=[('yard','Yard'),('foot','Foot')]
    input = forms.CharField (required=False, label=False, widget=forms.TextInput(attrs = {'type': 'number', 'placeholder' : "Enter the Number"}))
    measure1 = forms.CharField (
        label= '',widget = forms.Select(choices = CHOICES)
    )
    measure2 = forms.CharField(
        label='',widget = forms.Select (choices = CHOICES)
    )
    print("\nIt's working!",measure1,measure2)