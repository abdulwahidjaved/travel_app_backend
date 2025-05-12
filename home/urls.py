from django.urls import path
from home import views
from django.conf.urls.static import static 
from django.conf import settings 

urlpatterns = [
    path("home/", views.hello, name="hello"),
    path("home/login/", views.login_view, name="login"),
    path("home/logout/", views.logout_view, name="logout"),
    path("home/register/", views.register_view, name="register"),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
