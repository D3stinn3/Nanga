from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('profile/', views.profile_page, name="profile")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)