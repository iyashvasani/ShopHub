from io import open_code
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import CATEGORY_CHOICES, Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# def home(request):
#  return render(request, 'app/home.html')


class ProductView(View):
    def get(self, request):
        totalitem = 0
        trends = Product.objects.filter(category='T')
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        footwears = Product.objects.filter(category='FW')
        beautyproducts = Product.objects.filter(category='BP')
        furnitures = Product.objects.filter(category='F')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        consoles = Product.objects.filter(category='C')
        electronicsaccessories = Product.objects.filter(category='EA')
        games = Product.objects.filter(category='G')
        televisions = Product.objects.filter(category='TV')
        homeappliances = Product.objects.filter(category='HA')
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/home.html', {'trends': trends, 'topwears': topwears, 'bottomwears': bottomwears, 'footwears': footwears, 'beautyproducts': beautyproducts, 'furnitures': furnitures, 'mobiles': mobiles, 'laptops': laptops, 'consoles': consoles, 'electronicsaccessories': electronicsaccessories, 'games': games, 'televisions': televisions, 'homeappliances': homeappliances, 'totalitem': totalitem})

# def product_detail(request):
#  return render(request, 'app/productdetail.html')


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        totalitem = 0
        item_already_in_cart = False
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            item_already_in_cart = Cart.objects.filter(
                Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'app/productdetail.html', {'product': product, 'item_already_in_cart': item_already_in_cart, 'totalitem': totalitem})


@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')


@login_required
def show_cart(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        user = request.user
        cart = Cart.objects.filter(user=user)
        print(cart)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all()if p.user == user]
        print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount = amount + shipping_amount
            return render(request, 'app/addtocart.html', {'carts': cart, 'totalamount': totalamount, 'amount': amount, 'shipping_amount': shipping_amount, 'totalitem': totalitem})
        else:
            return render(request, 'app/emptycart.html', {'totalitem': totalitem})


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount,
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount,
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'amount': amount,
            'totalamount': amount + shipping_amount,
        }
        return JsonResponse(data)


@login_required
def buy_now(request):
    return render(request, 'app/buynow.html')


# def profile(request):
#     return render(request, 'app/profile.html')

@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/address.html', {'add': add, 'active': 'btn-primary', 'totalitem': totalitem})


@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/orders.html', {'order_placed': op, 'totalitem': totalitem})


# def passwordchange(request):
#     return render(request, 'app/passwordchange.html')


def trend(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        trends = Product.objects.filter(category='T')
    elif data == 'Beats' or data == 'Now' or data == 'Pemoe' or data == 'Rubiks' or data == 'Olay' or data == 'Handbag':
        trends = Product.objects.filter(category='T').filter(brand=data)
    elif data == 'below':
        trends = Product.objects.filter(
            category='T').filter(discounted_price__lt=1000)
    elif data == 'above':
        trends = Product.objects.filter(
            category='T').filter(discounted_price__gt=1000)
    return render(request, 'app/trend.html', {'trends': trends, 'totalitem': totalitem})


def mobile(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'Mi' or data == 'Samsung' or data == 'Apple' or data == 'Oneplus' or data == 'Celkon':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'below':
        mobiles = Product.objects.filter(
            category='M').filter(discounted_price__lt=25000)
    elif data == 'above':
        mobiles = Product.objects.filter(
            category='M').filter(discounted_price__gt=25000)
    return render(request, 'app/mobile.html', {'mobiles': mobiles, 'totalitem': totalitem})


def laptop(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        laptops = Product.objects.filter(category='L')
    elif data == 'AGB' or data == 'MSI' or data == 'Apple' or data == 'HP' or data == 'Dell' or data == 'Asus':
        laptops = Product.objects.filter(category='L').filter(brand=data)
    elif data == 'below':
        laptops = Product.objects.filter(
            category='L').filter(discounted_price__lt=25000)
    elif data == 'above':
        laptops = Product.objects.filter(
            category='L').filter(discounted_price__gt=25000)
    return render(request, 'app/laptop.html', {'laptops': laptops, 'totalitem': totalitem})


def console(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        consoles = Product.objects.filter(category='C')
    elif data == 'Sony' or data == 'Microsoft' or data == 'Nintendo':
        consoles = Product.objects.filter(category='C').filter(brand=data)
    elif data == 'below':
        consoles = Product.objects.filter(
            category='C').filter(discounted_price__lt=25000)
    elif data == 'above':
        consoles = Product.objects.filter(
            category='C').filter(discounted_price__gt=25000)
    return render(request, 'app/console.html', {'consoles': consoles, 'totalitem': totalitem})


def electronicsaccessorie(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        electronicsaccessories = Product.objects.filter(category='EA')
    elif data == 'Apple' or data == 'Belkin' or data == 'boAt' or data == 'Mi' or data == 'Ustraa' or data == 'Sandisk':
        electronicsaccessories = Product.objects.filter(
            category='EA').filter(brand=data)
    elif data == 'below':
        electronicsaccessories = Product.objects.filter(
            category='EA').filter(discounted_price__lt=10000)
    elif data == 'above':
        electronicsaccessories = Product.objects.filter(
            category='EA').filter(discounted_price__gt=10000)
    return render(request, 'app/electronicsaccessorie.html', {'electronicsaccessories': electronicsaccessories, 'totalitem': totalitem})


def television(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        televisions = Product.objects.filter(category='TV')
    elif data == 'Mi' or data == 'LG' or data == 'VU' or data == 'Samsung' or data == 'Sony' or data == 'Colors':
        televisions = Product.objects.filter(category='TV').filter(brand=data)
    elif data == 'below':
        televisions = Product.objects.filter(
            category='TV').filter(discounted_price__lt=25000)
    elif data == 'above':
        televisions = Product.objects.filter(
            category='TV').filter(discounted_price__gt=25000)
    return render(request, 'app/television.html', {'televisions': televisions, 'totalitem': totalitem})


def homeappliance(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        homeappliances = Product.objects.filter(category='HA')
    elif data == 'LG' or data == 'Panasonic' or data == 'Samsung' or data == 'Glen' or data == 'BlueStar' or data == 'Kent':
        homeappliances = Product.objects.filter(
            category='HA').filter(brand=data)
    elif data == 'below':
        homeappliances = Product.objects.filter(
            category='HA').filter(discounted_price__lt=25000)
    elif data == 'above':
        homeappliances = Product.objects.filter(
            category='HA').filter(discounted_price__gt=25000)
    return render(request, 'app/homeappliance.html', {'homeappliances': homeappliances, 'totalitem': totalitem})


def furniture(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        furnitures = Product.objects.filter(category='F')
    elif data == 'IKEA':
        furnitures = Product.objects.filter(category='F').filter(brand=data)
    elif data == 'below':
        furnitures = Product.objects.filter(
            category='F').filter(discounted_price__lt=10000)
    elif data == 'above':
        furnitures = Product.objects.filter(
            category='F').filter(discounted_price__gt=10000)
    return render(request, 'app/furniture.html', {'furnitures': furnitures, 'totalitem': totalitem})


def footwear(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        footwears = Product.objects.filter(category='FW')
    elif data == 'Nike' or data == 'Vans' or data == 'Converse' or data == 'Bata' or data == 'LifeStyle':
        footwears = Product.objects.filter(category='FW').filter(brand=data)
    elif data == 'below':
        footwears = Product.objects.filter(
            category='FW').filter(discounted_price__lt=1000)
    elif data == 'above':
        footwears = Product.objects.filter(
            category='FW').filter(discounted_price__gt=1000)
    return render(request, 'app/footwear.html', {'footwears': footwears, 'totalitem': totalitem})


def bottomwear(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        bottomwears = Product.objects.filter(category='BW')
    elif data == 'HM' or data == 'Lee' or data == 'DNMX' or data == 'BombayJeans' or data == 'Aero' or data == 'Roadster':
        bottomwears = Product.objects.filter(category='BW').filter(brand=data)
    elif data == 'below':
        bottomwears = Product.objects.filter(
            category='BW').filter(discounted_price__lt=1000)
    elif data == 'above':
        bottomwears = Product.objects.filter(
            category='BW').filter(discounted_price__gt=1000)
    return render(request, 'app/bottomwear.html', {'bottomwears': bottomwears, 'totalitem': totalitem})


def topwear(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        topwears = Product.objects.filter(category='TW')
    elif data == 'PeterEngland' or data == 'Dolphin' or data == 'PepeJeans' or data == 'Zara' or data == 'Shein' or data == 'Forever21':
        topwears = Product.objects.filter(category='TW').filter(brand=data)
    elif data == 'below':
        topwears = Product.objects.filter(
            category='TW').filter(discounted_price__lt=1000)
    elif data == 'above':
        topwears = Product.objects.filter(
            category='TW').filter(discounted_price__gt=1000)
    return render(request, 'app/topwear.html', {'topwears': topwears, 'totalitem': totalitem})


def game(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        games = Product.objects.filter(category='G')
    elif data == 'Sony':
        games = Product.objects.filter(category='G').filter(brand=data)
    elif data == 'below':
        games = Product.objects.filter(
            category='G').filter(discounted_price__lt=2500)
    elif data == 'above':
        games = Product.objects.filter(
            category='G').filter(discounted_price__gt=2500)
    return render(request, 'app/game.html', {'games': games, 'totalitem': totalitem})


def beautyproduct(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        beautyproducts = Product.objects.filter(category='BP')
    elif data == 'FairLovely' or data == 'MamaEarth' or data == 'WOW' or data == 'Garnier' or data == 'Ustraa' or data == 'Nykaa':
        beautyproducts = Product.objects.filter(
            category='BP').filter(brand=data)
    elif data == 'below':
        beautyproducts = Product.objects.filter(
            category='BP').filter(discounted_price__lt=250)
    elif data == 'above':
        beautyproducts = Product.objects.filter(
            category='BP').filter(discounted_price__gt=250)
    return render(request, 'app/beautyproduct.html', {'beautyproducts': beautyproducts, 'totalitem': totalitem})


# def login(request):
#     return render(request, 'app/login.html')


# def customerregistration(request):
#     return render(request, 'app/customerregistration.html')


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(
                request, 'Congratulations! Registration Successful')
            form.save()
        return render(request, 'app/customerregistration.html', {'form': form})


@login_required
def checkout(request):
    totalitem = 0
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    totalamount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        totalamount = amount + shipping_amount
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/checkout.html', {'add': add, 'totalamount': totalamount, 'cart_items': cart_items, 'totalitem': totalitem})


@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,  customer=customer,
                    product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary', 'totalitem': totalitem})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        totalitem = 0
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            mobile_number = form.cleaned_data['mobile_number']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, mobile_number=mobile_number,
                           locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Profile Updated Successfully!')
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary', 'totalitem': totalitem})

def contact(request):
    return render(request, 'app/contact.html')
