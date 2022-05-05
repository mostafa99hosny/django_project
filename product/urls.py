from django.urls import path,include
from . import views
urlpatterns = [
  path('',views.home,name='home'),
  path('category/<int:categoryid>/',views.categories,name='categories'),
  path('product/<int:productid>/',views.products,name='products'),

]
