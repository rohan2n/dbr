from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from dbr.models import UserProfile,DbaRoaster
from dbr.forms import UserForm, DateForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    user_list = User.objects.order_by('id')
    user_dict={'user_list':user_list}
    return render(request,'dbr/index.html', context=user_dict)

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()


            registered = True
        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request,'dbr/register.html',
                        {'user_form':user_form,
                         'registered':registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('dbr:dashboard'))
                #return render(request,'dbr/index.html')

            else:
                return HttpResponse('Account Not ACTIVE')

        else:
            print("Login Failed")
            print("Username {} and Password {}".format(username,password))
            return HttpResponse('Invalid Login Details')


    else:
        return render(request,'dbr/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('dbr:login'))

def dashboard(request):
    user_list = User.objects.order_by('id')
    user_dict={'user_list':user_list}
    return render(request,'dbr/dashboard.html', context=user_dict)

def date(request):
    if request.method == 'POST':
        date_form = DateForm(request.POST)
        if date_form.is_valid():
            date = date_form.save(commit=False)
            return ('roaster')
    else:
        date_form = DateForm()

    return render(request, 'dbr/date.html', {'date_form' :date_form})

    #return render(request, 'dbr/date.html'  {'date_form':date_form})


def roaster(request):
    roaster = DbaRoaster.objects.filter(date=request.POST.get('date', None))
    dba_roaster={'roaster':roaster}
    return render(request,'dbr/roaster.html', context=dba_roaster)
