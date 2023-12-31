from django.contrib import admin
from django.urls import re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


urlpatterns = i18n_patterns(
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^rosetta/', include('rosetta.urls')),
    
    re_path(r'^cart/', include('cart.urls')),
    re_path(r'^orders/', include('orders.urls')),
    re_path(r'^coupons/', include('coupons.urls')),
    re_path(r'^', include('shop.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
