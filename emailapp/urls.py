from .import views
from django.urls import path

urlpatterns = [
     path('',views.add,name="add"),
     path('mail',views.mail,name="mail")

]