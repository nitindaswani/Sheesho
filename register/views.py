import re
from django.shortcuts import render,redirect
from register.models import users
from django.contrib.auth.hashers import make_password
from django.contrib import messages
import random
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def register(request):
    # ✅ get next from URL (GET) or form (POST)
    next_url = request.POST.get('next') or request.GET.get('next')

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        raw_password = request.POST.get('password')
        number = request.POST.get('number')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')


        if not re.match(r'^(?=.*[A-Za-z]).{8,}$', raw_password):
            messages.error(
                request,
                "Password must be at least 8 characters long and contain at least one letter."
            )
            return redirect('register')
        if users.objects.filter(email=email).exists():
            messages.error(request, "User already registered. Please login.")

            # ✅ redirect to login WITH next
            if next_url:
                return redirect(f"/login/?next={next_url}")

            return redirect('login')
        
        # Generate OTP and prepare session data
        otp = str(random.randint(100000, 999999))
        request.session['registration_data'] = {
            'name': name,
            'email': email,
            'raw_password': raw_password,
            'number': number,
            'address': address,
            'city': city,
            'state': state,
            'pincode': pincode,
            'next_url': next_url
        }
        request.session['registration_otp'] = otp

        # Send OTP email
        try:
            send_mail(
                'Your Sheesho Registration OTP',
                f'Your One Time Password (OTP) for registration is {otp}.',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            messages.success(request, "OTP sent to your email. Please verify.")
            return redirect('verify_otp')
        except Exception as e:
            messages.error(request, "Error sending email. Please check your email address or try again later.")
            return redirect('register')

    return render(request, 'register.html')

def verify_otp(request):
    if 'registration_data' not in request.session or 'registration_otp' not in request.session:
        messages.error(request, "Session expired or invalid. Please register again.")
        return redirect('register')

    if request.method == "POST":
        user_otp = request.POST.get('otp')
        session_otp = request.session.get('registration_otp')

        if user_otp == session_otp:
            # Create user
            data = request.session['registration_data']
            users.objects.create(
                name=data['name'],
                email=data['email'],
                password=make_password(data['raw_password']),
                number=data['number'],
                address=data['address'],
                city=data['city'],
                state=data['state'],
                pincode=data['pincode']
            )
            
            # Clear session
            del request.session['registration_data']
            del request.session['registration_otp']

            messages.success(request, "Registered successfully! Please login.")
            
            next_url = data.get('next_url')
            if next_url:
                return redirect(f"/login/?next={next_url}")
            return redirect('login')
        else:
            messages.error(request, "Invalid OTP. Please try again.")
            return redirect('verify_otp')

    return render(request, 'verify_otp.html', {'email': request.session['registration_data']['email']})