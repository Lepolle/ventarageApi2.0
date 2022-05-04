from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# Api router
router = routers.DefaultRouter()

urlpatterns = [
    # Admin routes
    path('admin/', admin.site.urls),


    # Api routes
    path('api/', include('controlSesion.urls')),
    path('api/', include(router.urls)),
]
# Serve static files in development server
if settings.DEBUG:
    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)