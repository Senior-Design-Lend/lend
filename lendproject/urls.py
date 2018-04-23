"""lendproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from login import views
from home.views import homeView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', include('login.urls')),
    path('logout/', views.user_logout, name='logout'),
    path('home/', include('home.urls',namespace='home')),
    path('profile/', include('userprofile.urls'), name='profile'),
    path('items/', include('items.urls', namespace='items')),
    path('search/', include('haystack.urls')),
    path('transaction/', include('transaction.urls'), name='transaction'),
    path('postman', include('postman.urls'), name='postman'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
