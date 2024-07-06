from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from new_app.forms import FeedbackForm, work_updateForm, work_status, paymentform
from new_app.models import Customer, Feedback, Schedule, Booking, Create_work, Payment


@login_required(login_url='view_login')
def customer_profile(request):
    user = request.user

    data = Customer.objects.filter(user=user)

    return render(request,'customer/customer_profile.html',{'data':data})


@login_required(login_url='view_login')
def feedback(request):
    data = request.user
    user = Customer.objects.get(user = data)

    data = FeedbackForm()
    if request.method == 'POST':
         form = FeedbackForm(request.POST)

         if form.is_valid():
            obj = form.save(commit = False)
            obj.user = user
            obj.save()

    return render(request,'customer/feed.html',{'form':data})


@login_required(login_url='view_login')
def feedback_view(request):
    user = request.user.id
    customer = Customer.objects.get(user = user)

    data = Feedback.objects.filter(user=customer)
    return render(request,'customer/feedback_table.html',{"data":data})



@login_required(login_url='view_login')
def slotschedule(request):
    data = Schedule.objects.filter(status=0)
    return render(request,'customer/scheduletable.html', {"data": data})



@login_required(login_url='view_login')
def bookingschedule(request,id):
    data = Schedule.objects.get(id=id)
    u = Customer.objects.get(user = request.user)
    appointment = Booking.objects.filter(user = u,schedule=data)
    if appointment.exists():
        messages.info(request, 'already booked')
        return redirect('slotschedule')
    else:
        if request.method == 'POST':
            obj = Booking()
            obj.user=u
            obj.schedule=data
            obj.save()
            messages.info(request, 'successfully booked')
            return redirect('slotschedule')
    return render(request,'customer/appointment_table.html',{'schedule':data})


@login_required(login_url='view_login')
def customer_bookingview(request):
    user = request.user.id
    customer = Customer.objects.get(user=user)

    data = Booking.objects.filter(user=customer)
    return render(request,'customer/bookingview.html', {"bookingview": data})


@login_required(login_url='view_login')
def workstatus(request):

    user = request.user.id
    customer = Customer.objects.get(user = user)

    data = Create_work.objects.filter(customer = customer)
    return render(request,'customer/workstatus.html',{"workstatus":data})


@login_required(login_url='view_login')
def payment_field(request,id):
    data = paymentform()
    user = Create_work.objects.get(id=id)
    if request.method == 'POST':
        form = paymentform(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.data = user
            obj.save()
            user.pay = 1
            user.save()
            return redirect('workstatus')
    return render(request,'customer/pay.html',{'pay':data})


