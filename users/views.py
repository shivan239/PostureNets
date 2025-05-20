from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
import hashlib
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        pw    = request.POST['password']
        hashed = hashlib.sha256(pw.encode()).hexdigest()
        try:
            user = User.objects.get(email=email, password_hash=hashed)
            return redirect('dashboard')#HttpResponse(f"Welcome, {user.name}!")
        except User.DoesNotExist:
            return HttpResponse("Invalid credentials", status=401)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        name    = request.POST['username']
        email   = request.POST['email']
        pw      = request.POST['password']
        confirm = request.POST['confirmPassword']
        phone   = request.POST['country_code'] + request.POST['phone_number']

        if pw != confirm:
            return HttpResponse("Passwords do not match.", status=400)

        hashed = hashlib.sha256(pw.encode()).hexdigest()
        try:
            User.objects.create(
                name=name,
                email=email,
                password_hash=hashed,
                phone_number=phone
            )
            return HttpResponse("Registered successfully!")
        except Exception as e:
            return HttpResponse(f"Error: {e}", status=400)
    return redirect('index')

'''@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')'''


@login_required
def dashboard(request):
    user = request.user  # This gets the currently logged-in user
    context = {
        'name': user.get_full_name(),  # Or user.username if no full name
        'email': user.email,
        'date_joined': user.date_joined,
    }
    print(user.get_full_name(), user.email, user.date_joined)
    
    return render(request, 'dashboard.html', context)

