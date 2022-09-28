from django.urls import path
from . import views

# app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create/', views.create_tasks, name='create_tasks'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]
