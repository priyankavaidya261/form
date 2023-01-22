from django.urls import path
from . import views

urlpatterns = [
    path('',views.context),
    path('snippet',views.snippet_detail),
]
