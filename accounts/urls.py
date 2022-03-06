from django.urls import path
from . import views
urlpatterns = [
   path('', views.home, name='home'),
   path('index/', views.dashboard, name='index'),
   path('signup/', views.signup, name='signup'),
   path('signin/', views.signin, name='signin'),
   #path('signout/', views.signout, name='signout'),
]
