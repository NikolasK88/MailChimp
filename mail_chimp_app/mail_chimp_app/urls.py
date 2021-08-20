"""mail_chimp_app URL Configuration

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
from email_registration import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form1/', csrf_exempt(views.Form1View.as_view()), name='form1'),
    path('form1/list', csrf_exempt(views.Form1ListView.as_view()), name='form1_list'),
    path('form2/', csrf_exempt(views.Form2View.as_view()), name='form2'),
    path('form2/list', csrf_exempt(views.Form2ListView.as_view()), name='form2_list'),
]
