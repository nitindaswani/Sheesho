"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.urls import path
from app.views import *
from django.conf.urls.static import *
from django.conf import *
from django.contrib.staticfiles.urls import *

urlpatterns = [
    path('admin/', admin),
    path('',index),
    path('add_pro/',add_pro),
    path('update_pro/<pro_id>/',update_pro),
    path('delete_pro/<pro_id>/',delete_pro),
    path('order_success/<pro_id>/',order_sucess),
    path('order_placed/',order_placed),
    path('view_orders/',order_view),
    path('del_order/<order_id>',del_order),
    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()