from pyexpat.errors import messages
from django.shortcuts import render,redirect

from products.views import is_admin
from register.models import users
from .models import orders
from products.models import products
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

def place_orders(request,pro_name,pro_id):
    
    if not request.session.get("user_id"):
        return redirect(f"/login/?next={request.path}")

    user_id=request.session.get("user_id")
    context={"product":products.objects.get(pro_id=pro_id),
             "loggedin": bool(request.session.get("user_id")),
             "user" : users.objects.filter(id=user_id).first()}
    if request.method=='POST':
        data=request.POST
        name=data.get('name')
        email=data.get('email')
        address=data.get('address')
        city=data.get('city')
        state=data.get('state')
        zip_code=data.get('zip_code')
        phone=data.get('phone')
        
        
        phone = data.get("phone", "").strip()

        if not phone.isdigit() or len(phone) != 10:
            messages.error(request, "Invalid phone number")
            return redirect(request.path)

        user_id=users.objects.get()
        ord_pro_id=pro_id
        ord_price=products.objects.get(pro_id=pro_id).pro_price
        ord_pro_name=products.objects.get(pro_id=pro_id).pro_name
        
        o=orders(name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone,ord_pro_id=ord_pro_id,ord_price=ord_price,ord_pro_name=ord_pro_name,user_id=user_id)
        o.save()
        return redirect('/')
    
    
    return render(request,'place_order.html',context)



from django.shortcuts import render, redirect
from django.contrib import messages
from .models import orders

def user_orders(request, user_id, name):

    # 🔒 Require login
    session_user_id = request.session.get("user_id")
    if not session_user_id:
        return redirect(f"/login/?next={request.path}")

    # 🔒 Block access to other users' orders
    if str(session_user_id) != str(user_id):
        return redirect("/")

    # ✅ Fetch ONLY this user's orders
    orders_list = orders.objects.filter(user_uuid=user_id)

    context = {
        "orders": orders_list,
        "loggedin": True
    }

    return render(request, "user_orders.html", context)
