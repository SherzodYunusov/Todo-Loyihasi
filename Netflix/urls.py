"""
URL configuration for Netflix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app1.views import *
from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register("aktyorlar", AktyorModelViewSet)
router.register("kinolar", KinoModelViewSet)
router.register("Izohlar", IzohModelViewSet)
router.register("Izoh", IzohDeleteViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', obtain_auth_token),
    path('hello/', HelloApiView.as_view()),
    path('', include(router.urls)),
    path('aktyor/', AktyorApiView.as_view()),
    # path('aktyor/<int:pk>/', BittaAktyorApiView.as_view()),
    # path('aktyor/<int:pk>/delete', OchirishAktyorApiView.as_view()),
    path('izoh/', IzohApiView.as_view()),
    path('izoh/<int:pk>/', BittaIzohApiView.as_view()),
    path('kino/', KinoApiView.as_view()),
    # path('kinolar/<int:pk>/', KinoDetailApiView.as_view()),
    # path('kino/<int:pk>/delete', KinoDeleteApiView.as_view()),
    # path('kino/<int:pk>/', BittaKinoApiView.as_view()),


]
