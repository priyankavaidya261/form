from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('one/',include('newapp.urls')),
    path('admin/', admin.site.urls),
]
