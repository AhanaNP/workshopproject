from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from new_app.forms import FeedbackForm, ReplyForm, scheduleForm, work_assignForm
from new_app.models import Feedback, Schedule, Booking, Customer

@login_required(login_url='view_login')
def customer_feedback(request):

    data = Feedback.objects.all()
    return render(request, 'admin/admin_feedback_view.html', {"data": data})



@login_required(login_url='view_login')
def reply_feedback(request,id):
    feedback = Feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        feedback.reply = r
        feedback.save()
        messages.info(request,'reply send for complaint')
        # return redirect('customer_feedback')
    return render(request,'admin/feedupdate.html',{'feedback':feedback})

@login_required(login_url='view_login')
def scheduledetails(request):
    data = scheduleForm()
    if request.method =='POST':
        form = scheduleForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.info(request, 'schedule added')
            return redirect('scheduledata')
        else:
            messages.info(request, 'please enter valid date and time')

    return render(request,'admin/schedule.html',{'data':data})


@login_required(login_url='view_login')
def scheduledata(request):

    data = Schedule.objects.filter(status = 0)
    return render(request, 'admin/scheduletable.html', {"data": data})


@login_required(login_url='view_login')
def disable(request,id):
    data = Schedule.objects.get(id=id)
    data.status = 1
    data.save()
    return redirect('scheduledata')


@login_required(login_url='view_login')
def approved_view(request):
    data = Booking.objects.filter(status = 1)
    return render(request,'admin/assigntable.html',{'data':data})

@login_required(login_url='view_login')
def creatework(request,id):

    user = Booking.objects.get(id=id)
    customer = user.user
    form = work_assignForm()
    if request.method =='POST':
        form = work_assignForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer=customer
            obj.save()
            return redirect('approved')
    return render(request,'admin/creatework.html',{'create':form})

