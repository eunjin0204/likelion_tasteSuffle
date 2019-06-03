"""taste_shuffle URL Configuration

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
import user.views
import master.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user.views.main , name = 'main'),

    path('login/', master.views.login, name = 'login'),
    path('make/', master.views.make, name = 'make'),
    path('option/', master.views.option, name = 'option'),
    path('create/', master.views.create, name = 'create'),

    path('rooms/', user.views.rooms , name = 'rooms'),
    # path('rooms/', user.views.roomDetail , name = 'roomDetail'),
    path('rooms/<int:room_id>/', user.views.roomDetail , name = 'roomDetail'),
    path('result/<int:room_id>/', user.views.result , name = 'result'),
]