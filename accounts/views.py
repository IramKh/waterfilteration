from django.shortcuts import get_object_or_404, redirect, render
from accounts.models import *
from . forms import CustomerUpdateForm, CreateUserForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User
import socket
socket.getaddrinfo('localhost', 25)


# Create your views here.from django.http import HttpResponse


def home(request):
	temp= Our_Product.objects.all()
	temp1= Contact_Us.objects.all()
	if request.method=="POST":
		fname= request.POST['name']
		email= request.POST['email']
		subject= request.POST['subject']
		msg= request.POST['message']
		ins= Contact_Us(first_name=fname,email=email, subject=subject, message= msg)
		ins.save()

	return render (request, 'accounts/index.html',{'about':temp1,'abt':temp})

def testimonials(request):
    temp1= test_details.objects.all()

    return render(request, 'accounts/Testimonials.html', {'abt':temp1})

def products(request):
	temp= Our_Product.objects.all()
	return render (request, 'accounts/products.html',{'about':temp})

def about(request):
	temp=about_page.objects.all()
	return render (request, 'accounts/about.html',{'about':temp})

def contact(request):
	temp= Contact_Us.objects.all()
	temp1= Contact_Us.objects.all()
	if request.method=="POST":
		fname= request.POST['name']
		email= request.POST['email']
		subject= request.POST['subject']
		msg= request.POST['message']
		ins= Contact_Us(name=fname,email=email, subject=subject, message= msg)
		ins.save()
	return render (request, 'accounts/contact.html',{'about':temp1,'abt':temp})



def blog(request):
	temp=Blog_details.objects.all()
	return render (request, 'accounts/blog.html',{'about':temp})

def blog_post(request):
	return render (request, 'accounts/blog-post.html')

def checkout(request):
	return render (request, 'accounts/checkout.html')

def terms(request):
	temp=term_details.objects.all()
	return render (request, 'accounts/terms.html',{'about':temp})

def testimonials(request):
	temp=test_details.objects.all()
	return render (request, 'accounts/testimonials.html',{'about':temp})

def CustomerUpdate(request, pk):
    order=  Customer.objects.get(id=pk)
    form= CustomerUpdateForm(instance=order)
    if request.method == 'POST':
        form= CustomerUpdateForm(request.POST, instance= order)
        if form.is_valid:
            form.save()
            return redirect('/CustomerInfo/')
    context= {'form': form}
    return render(request, 'accounts/CustomerUpdate.html',context)

def customer_info(request):
    temp2= Customer.objects.all()
    return render(request, 'accounts/CustomerInfo.html',{'cus':temp2})


def CustomerDelete(request, pk):
    order= Customer.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/CustomerInfor')
    context= {'item': order}
    return render(request, 'accounts/CustomerDelete.html',context)

def messages(request):
	temp= Contact_Us.objects.all()

	context={'abt':temp}
	return render (request, 'accounts/messages.html' ,context)

def product_details(request, id):
    product= get_object_or_404(Our_Product,id=id)
    return render(request,'accounts/product-details.html', {'product':product})

def Admin_Login(request):
    return render(request,'accounts/Admin_Login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                
                return redirect('CustomerData')
        context = {'form':form}
        return render(request, 'accounts/Register.html', context)


def CustomerData(request):
    temp2= Customer.objects.all()
    if request.method=="POST":
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        Address= request.POST.get('address')
        number= request.POST['number']
        ins=Customer(Customer_first_name=fname,Customer_Email=email, Customer_Last_Name=lname, Customer_Address= Address,Customer_Contact_Number=number)
        ins.save()
        return redirect('Login')
    return render(request, 'accounts/CustomerData.html')




def post(self_, request):
	product = request.POST.get['product']
	print(product)
	return redirect('index')

def Login(request):
    if request.user.is_authenticated:
        return redirect('profile_user')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile_user')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'accounts/Login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('Login')








def store(request):
    template = render_to_string('accounts/email_template.html', {'name': request.user.username})
    email = EmailMessage(
        'Thanks for Purchasing',
        template,
        settings.EMAIL_HOST_USER,
        [request.user.email],
    )
    email.fail_silently=False
    email.send()

    cart = Cart(request)
    ab=request.session['cart']
    print(ab)
    req.objects.create()
    max_val=req.objects.latest('id')
    print(max_val)
    for key,value in ab.items():
        print(value['name'])

        orderel.objects.create(order=max_val, name=value['name'], quan=value['quantity'], price=value['price'])

    cart.clear()

    return render(request, 'accounts/success.html', {'cart': cart})

def cart_add(request, id):
    cart = Cart(request)
    product = Our_Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("main")



def item_clear(request, id):
    cart = Cart(request)
    product = Our_Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")



def item_increment(request, id):
    cart = Cart(request)
    product = Our_Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")



def item_decrement(request, id):
    cart = Cart(request)
    product = Our_Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")

def profile_user(request):
    abt= Customer.objects.all()
    return render(request, 'accounts/profile_user.html',{'abt': abt})



def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")



def cart_detail(request):
    return render(request, 'accounts/cart_detail.html')
