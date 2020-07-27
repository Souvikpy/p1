from django.urls import path
from myapp01 import views

app_name = "myapp01"

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('fact/<n>',views.fact,name='name'),
    path('child/', views.child, name='child'),
]
