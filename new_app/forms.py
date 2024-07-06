import datetime

from django import forms
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminTimeWidget
from django.contrib.auth.forms import UserCreationForm
from django.forms import TimeInput

from new_app.models import Login, Customer, Workmanager, Feedback, Schedule, Create_work, Payment


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)


    class Meta:
        model = Login
        fields = ('username','password1','password2')

class CustomerRegister(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ('user',)


class WorkmanagerRegister(forms.ModelForm):
    class Meta:
        model = Workmanager
        exclude = ('user',)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('feedback',)

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('reply',)

class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class scheduleForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    starting_time = forms.TimeField(widget=TimeInput)
    ending_time = forms.TimeField(widget=TimeInput)

    class Meta:
        model = Schedule
        fields = ('date','starting_time','ending_time')

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('starting_time')
        print(start)
        end = cleaned_data.get('ending_time')
        date = cleaned_data.get('date')

        if start > end:
            raise forms.ValidationError("End time should be greater than start time")

        if date < datetime.date.today():
            raise forms.ValidationError("Date can't be in the past")
        return cleaned_data


class work_assignForm(forms.ModelForm):
    class Meta:
        model = Create_work
        exclude = ('customer',)

class work_updateForm(forms.ModelForm):
    class Meta:
        model = Create_work
        exclude = ('workmanager','customer')


class work_status(forms.ModelForm):
    class Meta:
        model = Create_work
        exclude = ('customer',)


class paymentform(forms.ModelForm):
    expiry = forms.CharField(label='Expiry Date (MM/YY)', max_length=5, required=True,
                             widget=forms.TextInput(attrs={'placeholder':'(MM/YY)'}))
    class Meta:
        model = Payment
        exclude = ('data','pay')

