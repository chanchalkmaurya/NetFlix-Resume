
from django.contrib import admin
from django.urls import path, include
from netresume import views as net_views
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [
    path("", net_views.index, name="index"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
