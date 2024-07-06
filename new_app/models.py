from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_workmanager = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)


class Customer(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE,related_name='customer')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.name



class Workmanager(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='workmanager')
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=4)
    contact_no = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()
    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.name



class Feedback(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    feedback = models.TextField()
    date = models.DateField(auto_now=True)
    reply = models.TextField(null=True,blank=True)



class Schedule(models.Model):
    date = models.DateField()
    starting_time = models.TimeField()
    ending_time = models.TimeField()
    status = models.BooleanField(default=0)


class Booking(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    schedule = models.ForeignKey(Schedule,on_delete=models.DO_NOTHING)
    status = models.IntegerField(default=0)


class Create_work(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.DO_NOTHING, null=True)
    workmanager = models.ForeignKey('Workmanager', on_delete=models.DO_NOTHING, null=True)

    cat=(('M/C WITH GEAR','M/C WITH GEAR'),('M/C WITHOUT GEAR','M/C WITHOUT GEAR'),('LMV','LMV'),('FOUR WHEELER','FOUR WHEELER'))
    category = models.CharField(max_length=50,choices=cat,null=True, blank=True)

    vehicle_no = models.CharField(max_length=10,null=True, blank=True)
    vehicle_name = models.CharField(max_length=40,null=True, blank=True)
    vehicle_model = models.CharField(max_length=40,null=True, blank=True)
    vehicle_brand = models.CharField(max_length=40,null=True, blank=True)

    problem = models.CharField(max_length=40,null=True,blank=True)
    date = models.DateField(auto_now=True)
    cost = models.PositiveIntegerField(null=True, blank=True)



    sts=(('Repairing','Repairing'),('Repairing Done','Repairing Done'),('Released','Released'))
    status = models.CharField(max_length=50,choices=sts,default='Pending',null=True,blank = True)
    pay = models.IntegerField(default=0)


class Payment(models.Model):
    data = models.ForeignKey('Create_work', on_delete=models.DO_NOTHING)
    card_no = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    expiry = models.CharField(max_length=6)





















