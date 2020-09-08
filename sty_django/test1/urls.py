from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test1/', views.index),
]
