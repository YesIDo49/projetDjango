from django.urls import path
from . import views


app_name ='shopCrud'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path('add/addproduct/', views.addproduct, name='addrecord'),
    path('delete/<int:item_id>', views.delete, name='delete'),

]
