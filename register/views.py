import re
from django.shortcuts import render,redirect
from register.models import users
from django.contrib.auth.hashers import make_password
from django.contrib import messages

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
        
        users.objects.create(
            name=name,
            email=email,
            password=make_password(raw_password),
            number=number,
            address=address,
            city=city,
            state=state,
            pincode=pincode
        )

        messages.success(request, "Registered successfully! Please login.")

        # ✅ after register, go to login WITH next
        if next_url:
            return redirect(f"/login/?next={next_url}")

        return redirect('login')

    return render(request, 'register.html')