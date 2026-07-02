from os import name

from django.contrib import admin
from django.urls import path

from page.views import get_car, detail_car, create_car

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',get_car,name='list'),
    path('detail/<int:pk>/',detail_car,name='detail'),
    path('detail/',create_car,name='create')
]
