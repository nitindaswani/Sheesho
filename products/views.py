from xml.etree.ElementInclude import include
from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from .models import products
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from home.models import Review
from orders.models import orders
# Create your views here.




# Check if user is admin
def is_admin(user):
    return user.is_authenticated and user.is_staff


@login_required(login_url='admin:admin_login')
@user_passes_test(is_admin, login_url='admin:admin_login')
def show_products(request):
    category = request.GET.get('category')
    categories = [
        ('electronics', 'Electronics'),
        ('fashion', 'Fashion'),
        ('footwear', 'Footwear'),
        ('home-kitchen', 'Home & Kitchen'),
        ('beauty', 'Beauty'),
        ('grocery', 'Grocery'),
        ('books', 'Books'),
        ('sports', 'Sports'),
        ('toys-baby', 'Toys & Baby'),
        ('automotive', 'Automotive'),
        ('jewellery', 'Jewellery'),
        ('accessories', 'Accessories'),
    ]
    if category:
        products_list = products.objects.filter(pro_category=category)
    else:
        products_list = products.objects.all()
    
    context = {
        'products': products_list,
        'categories': categories,
        'active_category': category
    }
    return render(request, 'show_products.html', context)
    




@login_required(login_url='admin:admin_login')
@user_passes_test(is_admin, login_url='admin:admin_login')
def add_product(request):
    if request.method == 'POST':
        pro_name = request.POST.get('pro_name')
        pro_desc = request.POST.get('pro_desc')
        pro_price = request.POST.get('pro_price')
        pro_category = request.POST.get('pro_category')
        pro_stock = request.POST.get('pro_stock')
        pro_image = request.FILES.get('pro_image')

        new_product = products(
            pro_name=pro_name,
            pro_desc=pro_desc,
            pro_price=pro_price,
            pro_category=pro_category,
            pro_stock=pro_stock,
            pro_image=pro_image
        )
        new_product.save()
        return redirect('products:show_products')
    return render(request, 'add_product.html',context={"categories":products.CATEGORY_CHOICES})


@login_required(login_url='admin:admin_login')
@user_passes_test(is_admin, login_url='admin:admin_login')
def delete_product(request, pro_id):
    products.objects.filter(pro_id=pro_id).delete()
    messages.success(request, "Product deleted successfully!")
    url = reverse('products:show_products')
    return redirect(f"{url}#delete-popup")







@login_required(login_url='admin:admin_login')
@user_passes_test(is_admin, login_url='admin:admin_login')
def update_product(request, pro_id):
    product = products.objects.get(pro_id=pro_id)
    reviews = Review.objects.filter(product=product).order_by('-created_at')
    if request.method == 'POST':
        product.pro_name = request.POST.get('pro_name')
        product.pro_desc = request.POST.get('pro_desc')
        product.pro_price = request.POST.get('pro_price')
        product.pro_category = request.POST.get('pro_category')
        product.pro_stock = request.POST.get('pro_stock')
        if 'pro_image' in request.FILES:
            product.pro_image = request.FILES.get('pro_image')
        product.save()
        return redirect('products:show_products')
    context = {
        'product': product,
        "categories":products.CATEGORY_CHOICES,
        'reviews': reviews,
    }
    return render(request, 'update_product.html', context)




@login_required(login_url='admin:admin_login')
@user_passes_test(is_admin, login_url='admin:admin_login')
def view_orders(request):
    context={"orders":orders.objects.all()}
    return render(request,'all_orders.html',context)