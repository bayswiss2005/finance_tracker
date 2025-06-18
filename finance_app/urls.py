from django.urls import path
from .import views
from .import auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'), 
    path('add_account/', views.add_account, name='add_account'), 
    path('add_category/', views.add_category, name='add_category'), 
    path('add_transaction/', views.add_transaction, name='add_transaction'), 
    path('register/', auth_views.register_View, name='register'),
    path('login/', auth_views.login_View, name='login'),
    path('logout/', auth_views.logout_View, name='logout'),


]