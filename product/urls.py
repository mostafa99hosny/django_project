from django.urls import path,include
from . import views
urlpatterns = [
  path('',views.home,name='home'),
  path('category/<int:categoryid>/',views.categories,name='categories'),
  path('product/<int:productid>/',views.products,name='products'),
  path('AllProducts',views.AllProducts,name='AllProducts'),
  path('addcart/<int:proid>/', views.addcart, name='addcarts'),
  path('cartitem/', views.cartitem, name='cartitem'),
  path('deleteitem/<int:proid>/', views.deleteitem, name='delete'),
]
