
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from . import views
 
urlpatterns = [
     path('', view= views.cart, name='cart'),   
     path('add_cart/<int:product_id>/', view= views.add_cart, name='add_cart' ),
]    

