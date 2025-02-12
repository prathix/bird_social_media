from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "app"
urlpatterns= [
    path('admin', admin.site.urls),
    path('', views.index, name='home'),
    path('register', views.registration_form, name='register'),
    path('login', views.login_form, name='login')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)