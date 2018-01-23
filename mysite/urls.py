from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('', include('wishlist.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]