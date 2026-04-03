from pyexpat.errors import messages
from django.shortcuts import render,redirect

from register.models import users
from .models import orders
from products.models import products
from django.contrib.auth.decorators import login_required
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
        user_id=request.session.get("user_id")
        
        
        phone = data.get("phone", "").strip()

        if not phone.isdigit() or len(phone) != 10:
            messages.error(request, "Invalid phone number")
            return redirect(request.path)

        ord_pro_id=pro_id
        ord_price=products.objects.get(pro_id=pro_id).pro_price
        ord_pro_name=products.objects.get(pro_id=pro_id).pro_name
        
        o=orders(name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone,ord_pro_id=ord_pro_id,ord_price=ord_price,ord_pro_name=ord_pro_name,user_id=user_id)
        o.save()
        return redirect('/')
    
    
    return render(request,'place_order.html',context)



def user_orders(request,user_id,name):
    if not request.session.get("user_id"):
        return redirect(f"/login/?next={request.path}")
    
    context={"orders":orders.objects.filter(name=name),"loggedin": bool(request.session.get("user_id"))}
    return render(request,'user_orders.html',context)