"""challenge_back URL Configuration

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
from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter
from users.views import UserList

router = DefaultRouter()
router.register(r'users', UserList, basename='User')
schema_view = get_swagger_view(title='User Challenge API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt')),
    url(r'^users/$', UserList.as_view(), name='users-list'),
    path('admin/', admin.site.urls),
]
