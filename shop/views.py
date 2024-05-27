from django.shortcuts import render,redirect 
from django.http import HttpResponse
from .models import Product,Contact,Login_Activity,Orders,OrderUpdate,AddCart
from math import ceil
from django.contrib.auth import authenticate,login
from django.core.paginator import Paginator
from django.views.generic import ListView


# Create your views here
def index(request):
    products = Product.objects.all()
    print("here")
    print (products)
    n = len(products)
    print(n)
    nSlides = (n // 3) + ceil((n / 3)-(n // 3))
    params= {'no_of_slides':nSlides, 'range':range(1,nSlides), 'product':products}
    #allProds =[[products, range(1, len(products)),nSlides],
            #   [products, range(1, len(products)),nSlides]]
    # params = {'allProds': allProds}
    if request.user.is_authenticated:
        #return render(request, 'shop/about.html')
        return render(request, 'shop/home.html' ,params)
    else:
        return render(request, 'shop/login.html') 
    
def login_view(request):
    print('hii1')
    user = ''
    print('hii2')
    if request.method == "POST":
        username = request.POST['username']
        pwd = request.POST['password']
        print("hi::")
        user = authenticate(username=username, password=pwd)
        print(user)
        if user is not None:
            login(request,user)
            login_detail= Login_Activity(username=username, password=pwd)
            login_detail.save()
            return render(request,'shop/home.html')
        else:
            return render(request, 'shop/login.html', {'error': 'Invalid'})   
    #if user is not None:
        #pass
       #return redirect('home')    
    #else:
       #return render(request, 'shop/login.html')  
    return render(request, 'shop/login.html', {'error': 'Invalid'})   
    
def about(request):
    return render(request, 'shop/about.html')

def prodct(request): 
    product = Product.objects.all()
    paginator = Paginator(product,4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number) 
    #page1 = paginator.page(1)
    #page2 = paginator.page(2)
    #page2.object_list
    params= {"page_obj": page_obj,'product':product}
    return render(request, 'shop/product.html',params)

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phoneno = request.POST.get('phoneno','')
        desc = request.POST.get('desc','')
        print(name,email,phoneno,desc)
        contact= Contact(name=name,email=email,phone=phoneno,desc=desc)
        contact.save()
    return render(request, 'shop/contact.html') 

def prodView(request,myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/productview.html', {'product':product[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')

def addcart(request,myid):
    product= Product.objects.filter(id=myid)
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phoneno = request.POST.get('number','')
        address = request.POST.get('address','')
        itemno = request.POST.get('itemno','')
        utem_name = request.POST.get('utem_name','')
        addcart= AddCart(name=name,email=email,number=phoneno, address= address, itemno= itemno,utem_name= utem_name)
        addcart.save()
        print('utem_name')
        print(utem_name)
    return render(request, 'shop/addcart.html',{'product':product[0]})

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        print('phone')
        print(phone)
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    return render(request, 'shop/checkout.html')

class ProductListView(ListView):
    paginate_by = 4
    model = Product  
    queryset = Product.objects.all() 
   
        