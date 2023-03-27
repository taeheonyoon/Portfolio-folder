from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from contents.views import HomeView
from contents.views import indexView, offersView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('apis/', include('apis.urls')),
    path('users/', include('users.urls')),
    path('contents/', include('contents.urls')),
    path('index/', include('contents.urls')),
    path('index/offers/', include('contents.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)