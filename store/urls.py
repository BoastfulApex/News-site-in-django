from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', ProfileLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('store/', store, name='store'),
    path('add/', NewsCreate.as_view(), name='add'),
    path('update/<int:pk>', NewsUpdate.as_view(), name='update'),
    path('delete/<int:pk>', NewsDelete.as_view(), name='delete'),
    path('<str:new_name>/', cart, name='cart'),
    path('<str:new_name>/<str:new_tag>/', tags, name='tags'),

]
