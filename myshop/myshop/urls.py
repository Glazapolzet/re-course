from django.contrib import admin
from django.urls import re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


urlpatterns = i18n_patterns(
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^rosetta/', include('rosetta.urls')),
    
    re_path(_(r'^cart/'), include('cart.urls')),
    re_path(_(r'^orders/'), include('orders.urls')),
    re_path(_(r'^coupons/'), include('coupons.urls')),
    re_path(r'^', include('shop.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

