from django.urls import path
from . import views


urlpatterns = [
     path('signin',views.signin,name="signin"),
    path('signup',views.signup,name="signup"),
    path('signout',views.signout,name="signout"),
    path('signin1',views.signin1,name="signin1"),
    path('signup1',views.signup1,name="signup1"),
    path('signout1',views.signout1,name="signout1")
]