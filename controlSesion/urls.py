from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'Users', BaseUserView, 'users')
router.register(r'Products', ProductsView, 'products')
router.register(r'Category', CategoryView,'categories')

urlpatterns = [
    path('', include(router.urls)),
    # Auth views
    path('auth/login/',
         LoginView.as_view(), name='auth_login'),

    path('auth/logout/',
         LogoutView.as_view(), name='auth_logout'),

    path('auth/signup/',
         SignupView.as_view(), name='auth_signup'),

    path('auth/reset/',
         include('django_rest_passwordreset.urls',
                 namespace='password_reset')),

    # Profile views
    path('user/profile/',
         ProfileView.as_view(), name='user_profile'),
]