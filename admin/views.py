from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        # Check user exists, is staff/admin
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('products:show_products')
        else:
            return render(
                request,
                'admin_login.html',
                {'error': 'Invalid admin credentials'}
            )

    return render(request, 'admin_login.html')




def admin_logout(request):
    logout(request)
    return redirect('admin:admin_login')