from django.urls import path
from django.conf.urls import handler404
from . import views

handler404=views.custom404
urlpatterns = [
    path("", views.main, name="main"),
    path('members/',views.members, name='members'),
    path('template/',views.testing, name='testing'),
    path('members/details/<int:id>',views.details,name='details'),
]
