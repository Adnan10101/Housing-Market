from django.urls import path
from . import views


urlpatterns =[
    path("",views.home,name = "home"),
    path("prediction/",views.about,name = "prediction"),
    path("login/",views.login_page),
    path("logout/",views.logout_page),
    path("register/",views.register_page),
]