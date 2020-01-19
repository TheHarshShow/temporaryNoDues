from django.urls import path
from applyPage import views

urlpatterns = [

    path('',views.index,name="index"),

]
