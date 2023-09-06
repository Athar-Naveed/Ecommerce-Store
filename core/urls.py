from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .forms import LoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout_user,name='logout_user'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name="login"),
    path('item/',include('item.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('inbox/',include('conversation.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
