from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from new_app.forms import LoginRegister, CustomerRegister, WorkmanagerRegister
from new_app.models import Customer, Workmanager


# Create your views here.
def home(request):
    return render(request,'index.html')

def login_1(request):
    return render(request,'index1.html')

def dash(request):
    return render(request,'index2.html')



def customer_reg(request):
    form1 = LoginRegister()

    form2 = CustomerRegister()
    if request.method == 'POST':
        form1 = LoginRegister(request.POST)
        form2 = CustomerRegister(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            user12 = form1.save(commit=False)
            user12.is_customer = True
            user12.save()
            user1 = form2.save(commit=False)
            user1.user = user12
            user1.save()
            return redirect('home')
    return render(request,'customer_register.html',{'form1': form1,'form2': form2})


def manager_login(request):
    form1 = LoginRegister()

    form2 = WorkmanagerRegister()
    if request.method == 'POST':
        form1 = LoginRegister(request.POST)
        form2 = WorkmanagerRegister(request.POST, request.FILES)

        if form1.is_valid() and form2.is_valid():
            user12 = form1.save(commit=False)
            user12.is_workmanager = True
            user12.save()
            user1 = form2.save(commit=False)
            user1.user = user12
            user1.save()
            return redirect('home')
    return render(request, 'workmanager_login.html', {'form1': form1, 'form2': form2})


# def login_page(request):
#     return render(request,'login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        # print(username)
        password = request.POST.get('pass')
        # print(password)
        user = authenticate(request,username=username,password=password)
        # print(user)

        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adminpage')
            elif user.is_workmanager:
                return redirect('profile_view')
            elif user.is_customer:
                return redirect('customer_profile')
        else:
            messages.info(request,'Invalid Credentials')
    return render (request,'login.html')



@login_required(login_url='view_login')
def adminpage(request):
    return render(request,'admin/adminbase.html')

@login_required(login_url='view_login')
def managerpage(request):
    return render(request,'workmanager/workmanagerbase.html')


@login_required(login_url='view_login')
def customerpage(request):
    return render(request,'customer/customerbase.html')


@login_required(login_url='view_login')
def customertable(request):
    data = Customer.objects.all()
    return render(request,'customer/customer_table.html',{'view':data})


@login_required(login_url='view_login')
def managertable(request):
    data = Workmanager.objects.all()
    return render(request,'workmanager/workmanager_table.html',{'view':data})

@login_required(login_url='view_login')
def managerupdate(request,id):
    data = Workmanager.objects.get(id=id)
    form = WorkmanagerRegister(instance=data)
    if request.method == 'POST':
        data = WorkmanagerRegister(request.POST,request.FILES, instance=data )
        if data.is_valid():
            data.save()
            return redirect('managertable')
    return render(request,'workmanager/update.html',{'update':form})


@login_required(login_url='view_login')
def managerdelete(request,id):
    data = Workmanager.objects.get(id=id)
    data.delete()
    return redirect('managertable')


@login_required(login_url='view_login')
def customerdelete(request,id):

    data = Customer.objects.get(id=id)
    data.delete()

    return redirect('customertable')


