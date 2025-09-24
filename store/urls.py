from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("" , view = views.store , name="store" ),
    path("<slug:category_slug>/" , view= views.store , name="products_by_category" ),
    path("<slug:category_slug>/<slug:product_slug>/" , view= views.product_details , name="product_details" ),
] 
# + static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)