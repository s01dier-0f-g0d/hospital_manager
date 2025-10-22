from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth import authenticate, update_session_auth_hash, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

def signup(request):
    if request.method == 'POST':
        User.objects.create_user(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            username = request.POST['username'],
            password = request.POST['password'],
        )
        messages.success(request,'You are Signed Up')
        return redirect('signin')
    return render(request,'signup.html')

def signin(request):
    if request.method == 'POST':
        customer = authenticate(request,
                          username = request.POST['username'],
                          password = request.POST['password'])
        if customer:
            login(request,customer)
            messages.success(request,'You are Logged In')
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials')
    return render(request,'signin.html')

@login_required(login_url='signin')
def profile(request):
    return render(request,'profile.html',{'customer':request.user})


@login_required(login_url='signin')
def updateProfile(request):
    if request.method == 'POST':
        customer = request.user
        customer.first_name = request.POST['first_name']
        customer.last_name = request.POST['last_name']
        customer.email = request.POST['email']
        customer.username = request.POST['username']
        customer.save()
        messages.success(request,'Profile Updated Successfully')
        return redirect('profile')
    return render(request,'updateProfile.html',{'customer':request.user})

@login_required(login_url='signin')
def updatePass(request):
    if request.method == 'POST':
        customer = request.user
        old_pass = request.POST['old_pass']
        new_pass = request.POST['new_pass']
        confirm_pass = request.POST['confirm_pass']
        if not customer.check_password(old_pass):
            messages.error(request,'Enter valid Old Password')
        elif old_pass == new_pass:
            messages.error(request,'Old Password cannot be same as New Password')
        elif old_pass!=new_pass and new_pass!=confirm_pass:
            messages.error(request,'New Password must be same as Confirm Password')
        else:
            customer.set_password(new_pass)
            customer.save()
            messages.success(request,'Password Changed Successfully')
            return redirect('profile')
    return render(request,'updatePass.html')

@login_required(login_url='signin')
def signout(request):
    logout(request)
    messages.success(request,'You are Logged Out')
    return redirect('signin')

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib import messages

def forgotPass(request):
    User = get_user_model()
    customer = None
    
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        
        # Validate that both fields are provided
        if not email or not username:
            messages.error(request, 'Please provide both email and username')
            return render(request, 'forgotPass.html')
        
        try:
            # Find user by email and username
            customer = User.objects.get(email=email, username=username)
            
            # If user exists, proceed with password change
            new_pass = request.POST.get('new_pass')
            confirm_pass = request.POST.get('confirm_pass')
            
            if not new_pass or not confirm_pass:
                messages.error(request, 'Please fill in both password fields')
                return render(request, 'forgotPass.html', {'customer': customer})
            
            if new_pass == confirm_pass:
                # Check if new password is different from old one
                if check_password(new_pass, customer.password):
                    messages.warning(request, 'New password cannot be the same as current password')
                    return render(request, 'forgotPass.html', {'customer': customer})
                
                # Set new password
                customer.set_password(new_pass)
                customer.save()
                
                messages.success(request, 'Password reset successful! Please login with your new password.')
                return redirect('signin')
            else:
                messages.error(request, 'Passwords do not match')
                return render(request, 'forgotPass.html', {'customer': customer})
                
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or username combination')
    
    return render(request, 'forgotPass.html', {'customer': customer})