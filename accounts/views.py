from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from accounts.forms import *
from orders.models import Order


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.full_name = form.cleaned_data.get('full_name')
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.profile.full_name = form.cleaned_data.get('full_name')
            user.profile.username = form.cleaned_data.get('username')
            user.profile.gender = form.cleaned_data.get('gender')
            user.email = form.cleaned_data.get('email')
            user.userName = form.cleaned_data.get('userName')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=user.username, password=raw_password)
            # login(request, user)
            return redirect('shop:product_list')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def detail_profile(request):
    return render(request, 'accounts/detail_profile.html')

def updateOrderToPaid(request, Order):
    order = Order.objects.get(id = Order.id)
    order.isPaid = request.POST['isPaid']
    order.save()
    
def updateOrderToDiliver(request, Order):
    order = Order.objects.get(id = Order.id)
    order.isDelivered = request.POST['isDelivered']
    order.save()
