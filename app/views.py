from multiprocessing import context
from django.shortcuts import render,redirect

# Create your views here.

from django.http import HttpResponse
from .models import *


def add_pro(request):
    if request.method=='POST':
        data=request.POST
        pro_id=data.get('pro_id')
        pro_name=data.get('pro_name')
        pro_desc=data.get('pro_desc')
        pro_price=data.get('pro_price')
        pro_image=request.FILES.get('pro_image')
        p=products(pro_id=pro_id,pro_name=pro_name,pro_desc=pro_desc,pro_price=pro_price,pro_image=pro_image)
        p.save()
        return redirect("/admin")
    return render(request,'add_pro.html')
        

def update_pro(request, pro_id):
    product = products.objects.get(pro_id=pro_id)
    context = {"product": product}

    if request.method == 'POST':
        data = request.POST        
        product.pro_name = data.get('pro_name')
        product.pro_desc = data.get('pro_desc')
        product.pro_price = data.get('pro_price')        
        pro_image = request.FILES.get('pro_image')
        
        if pro_image:
            product.pro_image = pro_image        
            
        product.save()
        return redirect("/admin/")        
    return render(request, 'update_pro.html', context)

        
def index(request):
    context={"products":products.objects.all()}
    return render(request,'index.html',context)

def admin(request):
    context={"products":products.objects.all()}
    return render(request,"admin.html",context)



def delete_pro(request,pro_id):
    products.objects.filter(pro_id=pro_id).delete()
    return redirect("/admin/")





def order_sucess(request,pro_id):
    context={"product":products.objects.get(pro_id=pro_id)}
    if request.method=='POST':
        data=request.POST
        name=data.get('name')
        email=data.get('email')
        address=data.get('address')
        city=data.get('city')
        state=data.get('city')
        zip_code=data.get('zip_code')
        phone=data.get('phone')
        ord_pro_id=pro_id
        ord_price=products.objects.get(pro_id=pro_id).pro_price
        ord_pro_name=products.objects.get(pro_id=pro_id).pro_name
        
        o=orders(name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone,ord_pro_id=ord_pro_id,ord_price=ord_price,ord_pro_name=ord_pro_name)
        o.save()
        return redirect('/order_placed')
    
    
    return render(request,'order_success.html',context)

def order_placed(request):
    return render(request,'order_placed.html',)
    
def order_view(request):
    context={"orders":orders.objects.all()}
    return render(request,'view_orders.html',context)

def del_order(request,order_id):
    orders.objects.filter(order_id=order_id).delete()
    return redirect("/view_orders")