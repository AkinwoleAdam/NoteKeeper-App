from django.urls import path
from . import views

urlpatterns = [
  
path('register/',views.register,name = 'register'),

path('login/',views.loginUser,name = 'login'),

path('logout/',views.logoutUser,name = 'logout'),

path('',views.index,name = 'index'),

path('new_note/',views.new_note,name = 'new_note'),

path('update_note/<str:pk>/',views.update_note,name = 'update_note'),

path('delete_note/<str:pk>/',views.delete_note,name = 'delete_note'),

path('404/',views.notFound,name = '404'),
]