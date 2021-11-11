from django.shortcuts import render, get_object_or_404,redirect
from shop.models import Category, Product
from payment.models import Review
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from wishlist.models import Wishlist, WishlistItem
from django.contrib.postgres.search import SearchVector
from .forms import PostForm
from django.core.mail import send_mail


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)

        products = products.filter(category=category)
    page = request.GET.get('page')
    paginator = Paginator(products, 6)
    try:
        products = paginator.page(page)

    except PageNotAnInteger:
        products = paginator.page(1)

    except EmptyPage:
        products = paginator.page(1)
    is_authenticated = request.user.is_authenticated
    print(is_authenticated)
    if is_authenticated:
        wishlist = Wishlist.objects.filter(user=request.user)

        return render(
            request,
            'shop/product/list.html',
            {
                'category': category,
                'categories': categories,
                'products': products,
                'wishlist': wishlist,
            #     'reviews' : review,
            }
        )

    else:
        return render(
            request,
            'shop/product/list.html',
            {
                'category': category,
                'categories': categories,
                'products': products,
                # 'reviews' : review,
            }
        )


def product_search(request):
    results = None
    try:
        query = request.POST['query']
        results = Product.objects.filter(name__icontains=query) |\
            Product.objects.filter(description__icontains=query)
        page = request.GET.get('page')
        paginator = Paginator(results, 6)
        try:
            results = paginator.page(page)

        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:

            results = paginator.page(1)

        wishlist = None
        return render(
            request,
            'shop/product/list.html',
            {'products': results, 'wishlist': wishlist}
        )
    except KeyError:
        wishlist = None
        "KeyError"
        return render(
            request,
            'shop/product/list.html',
            {'products': results, 'wishlist': wishlist}
        )


def product_detail(request, id, slug):

    product = get_object_or_404(
        Product,
        id=id,
        slug=slug,
        available=True
    )
    # reviews = get_object_or_404(Review, product_id=id )
    reviews = product.review_set.all()
    # s_review = product.review.count()
    return render(
        request,
        'shop/product/detail.html',
        {'product': product,
         'reviews' : reviews
        }
    )
def share_post(request, product_id):
        current_product = get_object_or_404(Product, id=product_id)
        form = PostForm()
        if request.POST:
            postForm = PostForm(request.POST)
            if postForm.is_valid():
                from_mail = request.user.email
                title = postForm.cleaned_data['tittle']
                email_receive = postForm.cleaned_data['email_receive']
                body = postForm.cleaned_data['body']
                body += '\n'+'http://localhost:8000'+current_product.get_absolute_url()
                send_mail(title,body, from_mail, [email_receive])
                return redirect(current_product)
        return render(request,'shop/product/form_sendMail.html',{'form':form,})