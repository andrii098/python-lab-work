
from django.contrib import admin
from django.urls import path, include
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('shop/', include('shop.urls')),
    path('cart/', include('cart.urls')), 
    path('', views.index)
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
