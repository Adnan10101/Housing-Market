from django.urls import path
from . import views


urlpatterns =[
    path("",views.home,name = "home"),
    path("prediction/",views.about,name = "prediction"),
    path("login_page/",views.loginPage),
    path("register_page/",views.register)
]