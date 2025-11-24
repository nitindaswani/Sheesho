from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import products, orders


def add_pro(request):
    if request.method == 'POST':
        try:
            data = request.POST
            pro_name = data.get('pro_name', '').strip()
            pro_desc = data.get('pro_desc', '').strip()
            pro_price = data.get('pro_price', '').strip()
            pro_image = request.FILES.get('pro_image')

            if not all([pro_name, pro_desc, pro_price, pro_image]):
                messages.error(request, 'All fields are required.')
                return render(request, 'add_pro.html')

            try:
                price = float(pro_price)
                if price <= 0:
                    messages.error(request, 'Price must be greater than zero.')
                    return render(request, 'add_pro.html')
            except ValueError:
                messages.error(request, 'Invalid price format.')
                return render(request, 'add_pro.html')

            p = products(pro_name=pro_name, pro_desc=pro_desc, pro_price=price, pro_image=pro_image)
            p.save()
            messages.success(request, f'Product "{pro_name}" added successfully!')
            return redirect("/admin")
        except Exception as e:
            messages.error(request, f'Error adding product: {str(e)}')
            return render(request, 'add_pro.html')

    return render(request, 'add_pro.html')
        

def update_pro(request, pro_id):
    product = get_object_or_404(products, pro_id=pro_id)
    context = {"product": product}

    if request.method == 'POST':
        try:
            data = request.POST
            pro_name = data.get('pro_name', '').strip()
            pro_desc = data.get('pro_desc', '').strip()
            pro_price = data.get('pro_price', '').strip()
            pro_image = request.FILES.get('pro_image')

            if not all([pro_name, pro_desc, pro_price]):
                messages.error(request, 'Name, description, and price are required.')
                return render(request, 'update_pro.html', context)

            try:
                price = float(pro_price)
                if price <= 0:
                    messages.error(request, 'Price must be greater than zero.')
                    return render(request, 'update_pro.html', context)
            except ValueError:
                messages.error(request, 'Invalid price format.')
                return render(request, 'update_pro.html', context)

            product.pro_name = pro_name
            product.pro_desc = pro_desc
            product.pro_price = price

            if pro_image:
                product.pro_image = pro_image

            product.save()
            messages.success(request, f'Product "{pro_name}" updated successfully!')
            return redirect("/admin/")
        except Exception as e:
            messages.error(request, f'Error updating product: {str(e)}')
            return render(request, 'update_pro.html', context)

    return render(request, 'update_pro.html', context)

        
def index(request):
    search_query = request.GET.get('search', '').strip()
    all_products = products.objects.all().order_by('-pro_id')

    if search_query:
        all_products = all_products.filter(
            Q(pro_name__icontains=search_query) | Q(pro_desc__icontains=search_query)
        )

    paginator = Paginator(all_products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "products": page_obj,
        "search_query": search_query,
        "page_obj": page_obj
    }
    return render(request, 'index.html', context)

def admin(request):
    search_query = request.GET.get('search', '').strip()
    all_products = products.objects.all().order_by('-pro_id')

    if search_query:
        all_products = all_products.filter(
            Q(pro_name__icontains=search_query) | Q(pro_desc__icontains=search_query)
        )

    paginator = Paginator(all_products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "products": page_obj,
        "search_query": search_query,
        "page_obj": page_obj
    }
    return render(request, "admin.html", context)



def delete_pro(request, pro_id):
    product = get_object_or_404(products, pro_id=pro_id)
    product_name = product.pro_name
    product.delete()
    messages.success(request, f'Product "{product_name}" deleted successfully!')
    return redirect("/admin/")





def order_sucess(request, pro_id):
    product = get_object_or_404(products, pro_id=pro_id)
    context = {"product": product}

    if request.method == 'POST':
        try:
            data = request.POST
            name = data.get('name', '').strip()
            email = data.get('email', '').strip()
            address = data.get('address', '').strip()
            city = data.get('city', '').strip()
            state = data.get('state', '').strip()
            zip_code = data.get('zip_code', '').strip()
            phone = data.get('phone', '').strip()

            if not all([name, email, address, city, state, zip_code, phone]):
                messages.error(request, 'All fields are required.')
                return render(request, 'order_success.html', context)

            if len(phone) < 10:
                messages.error(request, 'Phone number must be at least 10 digits.')
                return render(request, 'order_success.html', context)

            o = orders(
                name=name,
                email=email,
                address=address,
                city=city,
                state=state,
                zip_code=zip_code,
                phone=phone,
                ord_pro_id=pro_id,
                ord_price=product.pro_price,
                ord_pro_name=product.pro_name
            )
            o.save()
            messages.success(request, 'Order placed successfully!')
            return redirect('/order_placed')
        except Exception as e:
            messages.error(request, f'Error placing order: {str(e)}')
            return render(request, 'order_success.html', context)

    return render(request, 'order_success.html', context)

def order_placed(request):
    return render(request,'order_placed.html',)
    
def order_view(request):
    search_query = request.GET.get('search', '').strip()
    all_orders = orders.objects.all().order_by('-order_id')

    if search_query:
        all_orders = all_orders.filter(
            Q(name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(ord_pro_name__icontains=search_query) |
            Q(order_id__icontains=search_query)
        )

    paginator = Paginator(all_orders, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "orders": page_obj,
        "search_query": search_query,
        "page_obj": page_obj
    }
    return render(request, 'view_orders.html', context)

def del_order(request, order_id):
    order = get_object_or_404(orders, order_id=order_id)
    order_info = f"Order #{order_id} for {order.name}"
    order.delete()
    messages.success(request, f'{order_info} deleted successfully!')
    return redirect("/view_orders")