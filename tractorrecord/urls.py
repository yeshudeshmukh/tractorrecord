"""tractorrecord URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page,name="home"),
    path('<int:pk>',views.detail_page,name="detail"),
    path('registration/',views.registration_page,name="registration"),
    path('login/',views.login_page,name="login"),
    path('tractorreg/',views.tractorreg_page,name="tractorreg"),
    path('logout/',views.logout_page,name='logout')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
