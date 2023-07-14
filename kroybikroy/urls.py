from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'


urlpatterns = [
    path('',include('main.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('items/',include('item.urls')),
    path('inbox/',include('chat.urls')),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)