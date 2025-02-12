from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import *
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,"index.html")

@login_required
def admin_homepage(request):
    return render(request,"admin_homepage.html")

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            auth_login(request,user)
            return redirect('admin_homepage')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request,"admin_login.html")

def user_login(request):    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('user_dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request,"user_login.html")

@login_required
def booking(request,train_id): 
    train = Train.objects.get(id=train_id)   
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.train = train
            ticket.save()
            messages.success(request, 'Ticket Booked Successfully')
            return redirect('view_ticket')
        else:
            messages.error(request, 'Invalid form')
    else:
        form = BookingForm()
    return render(request,"booking.html",{'form':form,'train':train})

@login_required
def train_list(request):    
    trains = Train.objects.all()
    return render(request,"trains_list.html",{'trains':trains})

@login_required
def add_schedule(request):
    stations = Station.objects.all()  # Get all available stations
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Schedule added successfully!')
            return redirect('train_schedule', train_id=form.cleaned_data['train'].id)
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = ScheduleForm()
    return render(request, "add_schedule.html", {'form': form, 'stations': stations})  # Pass stations to the template

@login_required
def train_schedule(request, train_id):
    train = Train.objects.get(id=train_id)
    schedule = train.schedules.all()
    return render(request,"train_schedule.html",{'train':train,'schedule':schedule})

def register(request):    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_confirm']:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])  # Set the password properly
                user.save()
                auth_login(request, user)
                return redirect('user_dashboard')
            else:
                messages.error(request, 'Passwords do not match.')
    else:
        form = UserRegistrationForm()
    return render(request,"register.html", {'form': form})


@login_required
def password_reset(request):    
    return render(request,"password_reset.html")

@login_required
def user_dashboard(request):    
    user = request.user
    bookings = Ticket.objects.filter(passenger_name=user)  # Assuming there's a Booking model with a user field
    return render(request, "user_dashboard.html", {
        'username': user.username,
        'email': user.email,
        'bookings': bookings,
    })


@login_required
def view_ticket(request):    
    return render(request,"view_ticket.html")

@login_required
def logout(request):
    auth_logout(request)
    return redirect('trains_list')

@login_required

def add_station(request):
    if request.method == 'POST':
        form = StationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_homepage')
    else:
        form = StationForm()
    return render(request, 'add_station.html', {'form': form})

@login_required
def add_train(request):
    if request.method == 'POST':
        form = TrainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_homepage')
    else:
        form = TrainForm()
    return render(request, 'add_train.html', {'form': form})