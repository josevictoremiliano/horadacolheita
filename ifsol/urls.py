from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


app_name = "ifsol"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("feira.urls", namespace="feira")),
    path("", include("users.urls", namespace="users")),



    
]

urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)