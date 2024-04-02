from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views import View
from django.conf import settings
from .models import Product,Cart,Customer,Order_placed,Feedback
from .forms import CustomerRegistrationForm,Customer_Profile,FeedbackForm,PaymentForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import random
from django.db.models import Q

# Home And Index Both are display Home Page
class Home(View):
    def get(self, request):
        self.Tv = list(Product.objects.filter(category="Tv"))
        self.Mobile = list(Product.objects.filter(category="Mobile"))
        self.Laptop = list(Product.objects.filter(category="Laptop"))
        self.Camera = list(Product.objects.filter(category="Camera"))
        self.Tablet = list(Product.objects.filter(category="Tablet"))
        self.Speaker = list(Product.objects.filter(category="Speaker"))
        self.Smart_Watch = list(Product.objects.filter(category="Smart Watch"))
        self.Computer = list(Product.objects.filter(category="Computer"))

        random.shuffle(self.Tv)
        random.shuffle(self.Mobile)
        random.shuffle(self.Laptop)
        random.shuffle(self.Camera)
        random.shuffle(self.Tablet)
        random.shuffle(self.Speaker)
        random.shuffle(self.Smart_Watch)
        random.shuffle(self.Computer)

        context = {
            'Tv': self.Tv[:4],
            'Mobile': self.Mobile[:4],
            'Laptop': self.Laptop[:4],
            'Camera': self.Camera[:4],
            'Tablet': self.Tablet[:4],
            'Speaker': self.Speaker[:4],
            'Smart_Watch': self.Smart_Watch[:4],
            'Computer': self.Computer[:4]
        }

        return render(request, "app/home.html", context)


class Index(Home):
    def get(self, request):
        super().get(request)
        context = {
            'Tv': self.Tv,
            'Mobile': self.Mobile,
            'Laptop': self.Laptop,
            'Camera': self.Camera,
            'Tablet': self.Tablet,
            'Speaker': self.Speaker,
            'Smart_Watch': self.Smart_Watch,
            'Computer': self.Computer
        }
        # Add any additional context specific to the index view here
        return render(request, "app/index.html", context)
def About(request):
    return render(request,'app/about-us.html')

def contact(request):
    return render(request,'app/contact.html')

#this all are display catagory by products
def Mobile(request,data=None):
    if data==None:
        product=Product.objects.filter(category='Mobile')
    elif data=='Vivo' or data=='Oppo' or data=='Samsung' or data=='Apple' or data=='Redmi' or data=='Lava':
        product=Product.objects.filter(category='Mobile').filter(brand=data)
    elif data=='Above':
        product=Product.objects.filter(category='Mobile').filter(discount_price__gt=10000)
    elif data=='Below':
        product = Product.objects.filter(category='Mobile').filter(discount_price__lt=10000)
    elif data=='A-Z':
        product = Product.objects.filter(category='Mobile').order_by('title')
    elif data=='Low-High':
        product = Product.objects.filter(category='Mobile').order_by('discount_price')
    elif data=='High-Low':
        product = Product.objects.filter(category='Mobile').order_by('-discount_price')


    return render(request, 'app/mobile.html', {'data': product})

def Tv(request, data=None):
        if data == None:
            product = Product.objects.filter(category='Tv')
        elif data == 'Samsung' or data == 'Lg' or data == 'Sony' or data == 'OnePlus' or data == 'Mi':
            product = Product.objects.filter(category='Tv').filter(brand=data)
        elif data == 'Above':
            product = Product.objects.filter(category='Tv').filter(discount_price__gt=15000)
        elif data == 'Below':
            product = Product.objects.filter(category='Tv').filter(discount_price__lt=15000)
        elif data == 'A-Z':
            product = Product.objects.filter(category='Tv').order_by('title')
        elif data == 'Low-High':
            product = Product.objects.filter(category='Tv').order_by('discount_price')
        elif data == 'High-Low':
            product = Product.objects.filter(category='Tv').order_by('-discount_price')
        return render(request, 'app/tv.html', {'data': product})


def Laptop(request, data=None):
    if data == None:
        product = Product.objects.filter(category='Laptop')
    elif data == 'Acer' or data == 'Lenovo' or data == 'Hp' or data == 'Dell' or data == 'Asus':
        product = Product.objects.filter(category='Laptop').filter(brand=data)
    elif data == 'Above':
        product = Product.objects.filter(category='Laptop').filter(discount_price__gt=35000)
    elif data == 'Below':
        product = Product.objects.filter(category='Laptop').filter(discount_price__lt=35000)
    elif data=='A-Z':
        product = Product.objects.filter(category='Laptop').order_by('title')
    elif data=='Low-High':
        product = Product.objects.filter(category='Laptop').order_by('discount_price')
    elif data=='High-Low':
        product = Product.objects.filter(category='Laptop').order_by('-discount_price')
    return render(request, 'app/laptop.html', {'data': product})


def Camera(request, data=None):
    if data == None:
        product = Product.objects.filter(category='Camera')
    elif data == 'Canon' or data == 'Sony' or data == 'Nikon' or data == 'Panasonic' or data == 'Pentax':
        product = Product.objects.filter(category='Camera').filter(brand=data)
    elif data == 'Above':
        product = Product.objects.filter(category='Camera').filter(discount_price__gt=50000)
    elif data == 'Below':
        product = Product.objects.filter(category='camera').filter(discount_price__lt=50000)
    elif data=='A-Z':
        product = Product.objects.filter(category='Camera').order_by('title')
    elif data=='Low-High':
        product = Product.objects.filter(category='Camera').order_by('discount_price')
    elif data=='High-Low':
        product = Product.objects.filter(category='Camera').order_by('-discount_price')
    return render(request, 'app/camera.html', {'data': product})


def Speaker(request, data=None):
    if data == None:
        product = Product.objects.filter(category='Speaker')
    elif data == 'Sony' or data == 'Bose' or data == 'Jbl' or data == 'Harman' or data == 'Boat':
        product = Product.objects.filter(category='Speaker').filter(brand=data)
    elif data == 'Above':
        product = Product.objects.filter(category='Speaker').filter(discount_price__gt=10000)
    elif data == 'Below':
        product = Product.objects.filter(category='Speaker').filter(discount_price__lt=10000)
    elif data=='A-Z':
        product = Product.objects.filter(category='Speaker').order_by('title')
    elif data=='Low-High':
        product = Product.objects.filter(category='Speaker').order_by('discount_price')
    elif data=='High-Low':
        product = Product.objects.filter(category='Speaker').order_by('-discount_price')
    return render(request, 'app/speaker.html', {'data': product})


def SmartWatch(request, data=None):
    if data == None:
        product = Product.objects.filter(category='Smart Watch')
    elif data == 'Samsung' or data == 'Fireboltt' or data == 'Apple' or data == 'Garmin' or data == 'Amazfit':
        product = Product.objects.filter(category='Smart Watch').filter(brand=data)
    elif data == 'Above':
        product = Product.objects.filter(category='Smart Watch').filter(discount_price__gt=2000)
    elif data == 'Below':
        product = Product.objects.filter(category='Smart Watch').filter(discount_price__lt=2000)
    elif data=='A-Z':
        product = Product.objects.filter(category='Smart Watch').order_by('title')
    elif data=='Low-High':
        product = Product.objects.filter(category='Smart Watch').order_by('discount_price')
    elif data=='High-Low':
        product = Product.objects.filter(category='Smart Watch').order_by('-discount_price')
    return render(request, 'app/smart-watch.html', {'data': product})


def Tablet(request, data=None):
    if data == None:
        product = Product.objects.filter(category='Tablet')
    elif data == 'Asus' or data == 'Realme' or data == 'Samsung' or data == 'Apple' or data == 'OnePlus':
        product = Product.objects.filter(category='Tablet').filter(brand=data)
    elif data == 'Above':
        product = Product.objects.filter(category='Tablet').filter(discount_price__gt=10000)
    elif data == 'Below':
        product = Product.objects.filter(category='Tablet').filter(discount_price__lt=10000)
    elif data=='A-Z':
        product = Product.objects.filter(category='Tablet').order_by('title')
    elif data=='Low-High':
        product = Product.objects.filter(category='Tablet').order_by('discount_price')
    elif data=='High-Low':
        product = Product.objects.filter(category='Tablet').order_by('-discount_price')
    return render(request, 'app/tablet.html', {'data': product})



#this is show the product details

class  Product_details(View):
    def get(self,request,id):
        product=Product.objects.get(pk=id)

        if request.user.is_authenticated:
            already = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        else:
            already = False
        return render(request,'app/product_detail.html',{'data':product,'already':already})

#user register view
class CustomerRegisterView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'app/register.html',{'form':form})
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'ACCOUNT CREATED SUCCESSFULLY....!')
            form.save()
        return render(request,'app/register.html',{'form':form})

def user_log_out(request):
    logout(request)
    return redirect('/account/login')


@login_required()
def Password_Change_Success(request):
    return render(request,'app/pass-change-success.html')

@method_decorator(login_required,name='dispatch')
class Profile(View):
  def get (self,request):
     counts=0
     counts=Customer.objects.filter(user=request.user).count()
     form = Customer_Profile()
     address = Customer.objects.filter(user=request.user)
     if counts<2:
        context={'form':form,'add':address}
     else:
         context = {'add': address}
     return render (request,'app/profile.html',context)

  def post(self,request):
     form=Customer_Profile(request.POST)
     counts = 0
     counts = Customer.objects.filter(user=request.user).count()
     if counts < 2:
       if form.is_valid():
        user=request.user
        name=form.cleaned_data['name']
        location = form.cleaned_data['location']
        city=form.cleaned_data['city']
        state =form.cleaned_data['state']
        zipcode=form.cleaned_data['zipcode']
        reg=Customer(user=user,name=name,location=location,city=city,state=state,zipcode=zipcode)
        reg.save()
        messages.success(request,'profile updated successfully...........')
     address = Customer.objects.filter(user=request.user)
     if counts < 2:
        context={'form':form,'add':address}
     else:
        context = {'add': address}
     return render(request,'app/profile.html',context)

def Remove_Address(request,id):
    user = request.user

    add = Customer.objects.filter(user=user,id=id)
    print(add)
    add.delete()
    return redirect('profile')

@login_required()
def Add_To_Cart(request):
    if request.user.is_authenticated:
        user=request.user
        product_id=request.GET.get('product_id')
        product=Product.objects.get(id=product_id)
        Cart(user=user,product=product).save()
        #cart=Cart.objects.filter(user=user)
        return redirect('/show-cart')
    else:
        return redirect('/login')


@login_required()
def Show_Cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart_products=Cart.objects.filter(user=user)
        amount=0.0
        shipping_amount=49.0
        total_amount=0.0
        for cart_item in cart_products:
            temp_amount=(cart_item.product.discount_price * cart_item.quantity)
            amount+=temp_amount
        total_amount+=amount
        payable=total_amount+shipping_amount
        context={
            'carts':cart_products,
            'shipping':shipping_amount,
            'amount':amount,
            'total_amount':total_amount,
            'pay':payable,
            'is_empty':not cart_products.exists(),
        }
        return render(request,'app/show_cart.html',context)
    else:
        return HttpResponseRedirect('/account/login')
@login_required()
def update_cart(request):
    if request.method == 'POST':
        user = request.user
        for key,value in request.POST.items():
            if key.startswith('quantity_'):
                cart_id =key.split('_')[1]
                quantity=int(value)
                cart_item = Cart.objects.get(id=cart_id)
                cart_item.quantity = quantity
                cart_item.save()
        #messages.success(request,'cart update successfully')
    return redirect('show-cart')


def remove_cart(request):
    user = request.user
    print(user)
    p_id=request.GET.get('id')
    print(p_id)
    pro = Cart.objects.filter(user=user,id=p_id)
    print(pro)
    pro.delete()
    print("hello")
    return redirect('/show-cart')


@login_required()
def Check_Out(request):
    if request.user.is_authenticated:
        user=request.user
        address=Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        amount=0.0
        shipping_amount=50
        total_amount=0.0
        for cart_item in cart_items:
             temp_amount=(cart_item.product.discount_price * cart_item.quantity)
             amount+=temp_amount
        total_amount+=amount
        payble=total_amount+shipping_amount

        return render(request,'app/check_out.html',{'add':address,'total_amount':total_amount,'ship':shipping_amount,'pay':payble,'product':cart_items})
    else:
        return HttpResponseRedirect('/account/login')

@login_required()
def OrderPlace(request):
    user=request.user
    custid=request.GET.get('custid')
    customer=Customer.objects.get(id=custid)
    cart=Cart.objects.filter(user=user)
    
    add = Cart.objects.filter(user=user)
    for c in cart:
        Order_placed(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
        c.delete()
    return redirect('payment')

def Payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()
            return redirect('order')
    else:
        form = PaymentForm()
    return render(request, 'app/payment.html', {'form': form})
@login_required()
def Order(request):
    return render(request,'app/Orders.html')


def Cancel_order(request,id):
    user=request.user
    order_items = Order_placed.objects.filter(id=id)
    order_items.delete()
    return render(request,'app/order_cancel.html',{'order_item':order_items ,'order':order_items})



@login_required()
def My_Order(request):
    user=request.user
    order_items = Order_placed.objects.filter(user=user)
    return render(request,'app/my_orders.html',{'order':order_items})

def search(request):
    data=request.GET.get('search')
    result=None
    if data == 'Apple' or data == 'Samsung' or data == 'Lava' or data == 'Redmi' or data == 'Oppo' or data == 'Vivo':
        result = Product.objects.filter(category='Mobile').filter(brand=data)
    elif data == 'Mobile':
        result = Product.objects.filter(category=data)

    elif data == 'Laptop':
        result = Product.objects.filter(category=data)
    elif data == 'Dell' or data == 'Hp' or data == 'Lenovo' or data == 'Asus' or data == 'Acer':
        result = Product.objects.filter(category='Laptop').filter(brand=data)

    elif data == 'Tv':
        result = Product.objects.filter(category=data)
    elif data == 'Lg' or data == 'Samsung' or data == 'Sony' or data == 'Oneplus' or data == 'Mi':
        result = Product.objects.filter(category='Tv').filter(brand=data)

    elif data == 'Speaker':
        result = Product.objects.filter(category=data)
    elif data == 'Sony' or data == 'Bose' or data == 'Jbl' or data == 'Harman' or data == 'Boat':
        result = Product.objects.filter(category='Speaker').filter(brand=data)

    elif data == 'Tablet':
        result = Product.objects.filter(category=data)
    elif data == 'Samsung' or data == 'Apple' or data == 'Realme' or data == 'Asus' or data == 'Oneplus':
        result = Product.objects.filter(category='Tablet').filter(brand=data)

    elif data == 'Camera':
        result = Product.objects.filter(category=data)
    elif data == 'Canon' or data == 'Sony' or data == 'Nikon' or data == 'Panasonic' or data == 'Pentax':
        result = Product.objects.filter(category='Camera').filter(brand=data)

    elif data == 'Smart Watch' or data == 'Smart watch ':
        result = Product.objects.filter(category=data)
    elif data == 'Samsung' or data == 'Apple' or data == 'Fireboltt' or data == 'Garmin' or data == 'Titan':
        result = Product.objects.filter(category='Smart Watch').filter(brand=data)

    else:
        result = Product.objects.filter(title__contains=data)

    return render(request,'app/search.html',{'result':result})

@login_required()
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            user=request.user
            message = form.cleaned_data['message']
            reg = Feedback(user=user,message=message)
            reg.save()

        return redirect('feedback_thanks')
    else:
        form = FeedbackForm()

    return render(request, 'app/feedback_form.html', {'form': form})

def My_feedback(request):
    user=request.user
    feed=Feedback.objects.filter(user=user)
    print(feed)
    return render(request,'app/my_feed.html',{'feed':feed})




@login_required()
def feed_thank(request):
    return render(request,'app/feedback_thanks.html')




