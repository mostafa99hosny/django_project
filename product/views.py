from django.shortcuts import redirect, render
from . models import category,product,order
# Create your views here.
def home(request):
    allcategory = category.objects.all()
    allproducts = product.objects.all().order_by("-id")
    return render(request,'pages/Home.html',{"allcategory":allcategory,"allproducts":allproducts})
def categories(request,categoryid):
    allcategory = category.objects.all()
    mycategory = category.objects.get(id=categoryid)
    allproducts = product.objects.all().filter(category_id = categoryid ).order_by("-id")
    return render(request,'pages/category.html',{"allcategory":allcategory,"allproducts":allproducts,"mycategory":mycategory})
def products (request,productid):
    allcategory = category.objects.all()
    myproduct = product.objects.get(id=productid) 
    
    return render(request,'pages/product.html',{"allcategory":allcategory,"myproduct":myproduct})
def AllProducts(request):
    allcategory = category.objects.all()
    allproducts = product.objects.all().order_by("-id")
    return render(request,'pages/AllProducts.html',{"allcategory":allcategory,"allproducts":allproducts})

    

def addcart(request,proid):
    quantity=int(order.objects.filter(productid=proid).count())
    if quantity >= 1:
        ca=order.objects.get(productid=proid)
        order.objects.filter(productid=proid).update(num=int(ca.num)+1)
    else:
        id = request.user.id
        carts=order(productid=proid,user_id=id,num=1)
        carts.save()
    return redirect("/cartitem/")

def deleteitem(request,proid):
    item=order.objects.get(id=proid)
    item.delete()
    return redirect("/cartitem/")

def cartitem(request):
    quantity = 0
    price =0
    products = product.objects.all()
    orderss = order.objects.filter(user_id=request.user.id)
    for v in orderss:
        quantity=quantity+int(v.num)
        for f in product.objects.all():
            if v.productid ==f.id:
                price =price +(int(f.price)*int(v.num))
    return render(request, 'pages/cartitem.html',{"products":products,'quantity':quantity,"price":price,"orders":orderss})