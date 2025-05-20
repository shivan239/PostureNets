from django.urls import path, include
from . import views
from .views import dashboard
from django.contrib.auth.views import LogoutView

urlpatterns = [
  path('',        views.index,    name='index'),
  path('login/',  views.login,    name='login'),
  path('register/', views.register, name='register'),
  path('auth/', include('social_django.urls', namespace='social')),
  path('dashboard/', dashboard, name='dashboard'),
   path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
  
]
