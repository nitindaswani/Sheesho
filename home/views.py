from django.shortcuts import render,redirect
from products.models import *
from .models import Review
from register.models import users
# Create your views here.

def index(request):
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
    user = None
    user_id = request.session.get("user_id")
    if user_id:
        user = users.objects.filter(id=user_id).first()
        if not user:
            request.session.flush()  # 💣 kill broken session
    
    context = {
        'products': products_list,
        'categories': categories,
        'active_category': category,
        'loggedin': bool(user),
        'user': user,
    }
    
    return render(request, "index.html",context)


























def about(request):
    context={"loggedin": bool(request.session.get("user_id"))}
    return render(request, "about.html",context)




def product_detail(request, pro_name, pro_id):
    try:
        product = products.objects.get(pro_id=pro_id)
    except products.DoesNotExist:
        return redirect('home:index')

    # 🔹 check login via session
    loggedin = bool(request.session.get("user_id"))

    # 🔹 fetch all reviews for this product
    reviews = Review.objects.filter(product=product).order_by('-created_at')

    # 🔹 handle review submit
    if request.method == "POST":
        if not loggedin:
            return redirect(f"/login/?next={request.path}")

        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        user = users.objects.get(id=request.session['user_id'])

        Review.objects.create(
            product=product,
            user=user,
            rating=rating,
            comment=comment
        )

        # redirect to avoid duplicate submit on refresh
        return redirect(request.path)

    context = {
        'product': product,
        'reviews': reviews,
        'loggedin': loggedin,
    }

    return render(request, "product_detail.html", context)