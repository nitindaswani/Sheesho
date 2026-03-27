from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from register.models import users

# Create your views here.


def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email').lower().strip()
        password = request.POST.get('password').strip()
        
        next_url = request.POST.get('next') or request.GET.get('next')

        try:
            user = users.objects.get(email=email)

            from django.contrib.auth.hashers import check_password
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email
                if next_url:
                    return redirect(next_url)
                return redirect('/')

            else:
                messages.error(request, "Invalid password")

        except users.DoesNotExist:
            messages.error(request, "Email not registered")

        if next_url:
            return redirect(f"/login/?next={next_url}")
        return redirect('login')

    return render(request, 'login.html')

# def logout_user(request):
#     next_url = request.GET.get('next') or request.META.get('HTTP_REFERER', '/')
#     request.session.flush()
#     return redirect('/')

def logout_user(request):
    # Remove ONLY user session keys
    request.session.pop('user_id', None)
    request.session.pop('user_name', None)
    request.session.pop('user_email', None)

    return redirect('/')
