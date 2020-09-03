
from django.urls import path
from . import views


app_name = 'blogg'

urlpatterns = [

    path('', views.all_bloggs, name = 'all_bloggs'),
    path('<int:blog_id>/', views.detail, name = 'detail'),

]