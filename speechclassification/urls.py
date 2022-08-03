"""speechclassification URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', RedirectView.as_view(url='/dashboard'), name='home'),
    path('dashboard/', include('dashboard.urls')),
    path('grade/', include('grade.urls')),
    path('audio/', include('audio.urls')),
    path('transcribe/', include('transcribe.urls')),
    path('tugas_2/', include('tugas_2.urls')),
    path('message/', include('message.urls')),
    path('message/', include('message.urls')),
    path('workplace_user_network/', include('workplace_user_network.urls')),
    path('api/', include('snippets_api.urls')),
    
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls), 
    path('tugas6/', include('tugas6.urls')),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
