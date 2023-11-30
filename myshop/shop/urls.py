from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    
    re_path(r'^shop/', include([
        path(r'', views.product_list, name="product_list"),
        path(r'<slug:category_slug>', views.get_category, name="get_category"),
        path(r'<slug:category_slug>/<slug:product_slug>/<product_id>', views.get_product, name="get_product")
    ]))
]
