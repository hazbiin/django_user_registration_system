from django.urls import path
from .import views

urlpatterns=[
   path("",views.loginPage,name='login'),
    path('signup/',views.SignupPage,name="signup"),
    path('home/',views.HomePage,name="home"),
    path('logout/',views.LogoutPage,name="logout")
]
