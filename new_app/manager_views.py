from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from new_app.forms import work_assignForm, work_updateForm
from new_app.models import Workmanager, Booking, Create_work


@login_required(login_url='view_login')
def profile_view(request):
    user = request.user
    data = Workmanager.objects.filter (user=user)


    return render(request,'workmanager/profile_view.html',{'data':data})

@login_required(login_url='view_login')
def booking_view(request):
    data = Booking.objects.all()
    return render(request,'workmanager/bookingview.html',{'view':data})


@login_required(login_url='view_login')
def approval(request,id):
    data = Booking.objects.get(id=id)
    # if request.method == 'POST':
    data.status = 1
    data.save()
    return redirect('booking_view')


@login_required(login_url='view_login')
def reject(request,id):
    data = Booking.objects.get(id=id)
    data.status = 2
    data.save()
    return redirect('booking_view')


@login_required(login_url='view_login')
def manager_workview(request):
    user = request.user
    workmanager = Workmanager.objects.get(user = user)
    # print(workmanager)

    data = Create_work.objects.filter(workmanager = workmanager)
    # print(data)
    return render(request,'workmanager/workview.html',{'data':data})


@login_required(login_url='view_login')
def managerworkupdate(request,id):
    data = Create_work.objects.get(id=id)
    form = work_updateForm(instance=data)
    if request.method == 'POST':
        form = work_updateForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('manager_workview')
    return render(request,'workmanager/managerworkupdate.html',{'managerworkupdate':form})
