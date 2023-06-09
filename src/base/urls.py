from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('profile/', views.profile_page, name="profile"),
    path('signin/', views.signup_page, name="signin"),
    path('', views.landing_page, name="home"),
    path('account/', views.account_page, name="account")
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)