from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('profile/', views.profile_page, name="profile"),
    path('signin/', views.signup_page, name="signin"),
    path('account/<str:pk>/', views.account_page, name="account")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)