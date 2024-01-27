from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import PizzaModel,OrderModel
from django.contrib.auth.models import User

# Create your views here.
def adminloginview(request):
    return render(request,'pizzaapp/adminlogin.html')

def authenticateadmin(request):
    username=request.POST['username']
    password=request.POST['password']

    user= authenticate(username=username,password=password)

    #if user exists
    if user is not None and user.username=="vivek":
        login(request,user)
        return redirect('adminhomepage')
    
    #if user does not exists
    if user is None:
        messages.add_message(request,messages.ERROR,"invalid credentials")
        return redirect('adminloginpage')

def adminhomepageview(request):
    if not request.user.is_authenticated:
        return redirect('adminloginpage')
    context={'pizzas':PizzaModel.objects.all()}
    return render (request,"pizzaapp/adminhomepage.html",context)

def logoutadmin(request):
    logout(request)
    return redirect('adminloginpage')

def addpizza(request):
    #code to add the pizza into the database
    name=request.POST['pizza']
    price=request.POST['price']
    PizzaModel(name=name,price=price).save()
    return redirect('adminhomepage')

def deletepizza(request,pizzapk):
    #code to delete the pizza
    PizzaModel.objects.filter(id=pizzapk).delete()
    return redirect('adminhomepage')

def homepageview(request):
    #code to redirect user to homepage
    return render (request,"pizzaapp/homepage.html")

def signup(request):
    #code to add user signup information in the user database
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    username= request.POST['username']
    password=request.POST['password']
    email=request.POST['email']
    #if user already exists
    if User.objects.filter(username=username).exists():
        messages.add_message(request,messages.ERROR,"User already exists")
        return redirect('homepage')
    #if user does not exist
    User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email).save()
    messages.add_message(request,messages.ERROR,"User created")
    return redirect ('homepage')

def userloginview(request):
    return render(request,"pizzaapp/userlogin.html")

def userauthenticate(request):
    username=request.POST['username']
    password=request.POST['password']

    user= authenticate(username=username,password=password)

    #if user exists
    if user is not None:
        login(request,user)
        return redirect('customerpage')
    
    #if user does not exists
    if user is None:
        messages.add_message(request,messages.ERROR,"invalid credentials")
        return redirect('userlogin')

def customerwelcomeview(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    username=request.user.username
    context={'username':username,'pizzas':PizzaModel.objects.all()}
    return render(request,"pizzaapp/customerwelcome.html",context)

def logoutuser(request):
    logout(request)
    return redirect('userlogin')

def placeorder(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    username= request.user.username 
    address= request.POST['address']
    phoneno=request.POST['phoneno']
    ordereditems=""
    for pizza in PizzaModel.objects.all():
        pizzaid=pizza.id
        name= pizza.name
        price= pizza.price
        quantity=request.POST.get(str(pizzaid)," ")
        status="PENDING"
        if str(quantity)!="0" and str(quantity)!=" ":
            ordereditems=ordereditems + name + "  " + "price: " + str(int(quantity)*int(price)) + "  quantity: " + quantity + "  "

    OrderModel(username=username,phone=phoneno,address=address,ordereditems=ordereditems,status=status).save()
    messages.add_message(request,messages.SUCCESS,"Order Successfully Placed")
    return redirect('customerpage')

def userorders(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    orders= OrderModel.objects.filter(username= request.user.username)
    context= {'orders': orders}
    return render (request,"pizzaapp/myorders.html",context)

def adminorders(request):
    if not request.user.is_authenticated and request.user.username=="vivek":
        return redirect('adminloginpage')
    orders=OrderModel.objects.all()
    context= {'orders': orders}
    return render (request,"pizzaapp/adminorders.html",context)

def acceptorder(request,orderpk):
    order=OrderModel.objects.filter(id=orderpk)[0]
    order.status="ACCEPTED"
    order.save()
    return redirect(request.META['HTTP_REFERER'])

def declineorder(request,orderpk):
    order=OrderModel.objects.filter(id=orderpk)[0]
    order.status="DECLINED"
    order.save()
    return redirect(request.META['HTTP_REFERER'])