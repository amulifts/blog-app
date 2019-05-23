"""blog URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home path('', Home.as_view(), name='home')
    2. Add a URL to urlpatterns:  
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.post import views as post_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("post/", include("apps.post.urls")),
    path("accounts/", include("apps.accounts.urls")),
    path("", post_view.index, name="home"),
]
