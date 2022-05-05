from django.shortcuts import render
from . models import category,product
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

# def mobiles(request,categoryid):
#     allcategory = category.objects.all()
#     allproducts = product.objects.all().filter(category_id = categoryid )
#     return render(request,'pages/mobile.html',{"allcategory":allcategory,"allproducts":allproducts})
# def laptop(request,categoryid):
#     allcategory = category.objects.all()
#     allproducts = product.objects.all().filter(category_id = categoryid )
#     return render(request,'pages/laptop.html',{"allcategory":allcategory,"allproducts":allproducts})