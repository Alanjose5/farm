from django.urls import path
from . import views
urlpatterns=[
    path('', views.demo, name="demo"),

    path('ee',views.cos,name="cos"),
    path('rr',views.tem,name="rr"),
    path('dd',views.register_request,name="dd"),
    path('login',views.login_request,name="login"),
    path('logout',views.logout_request,name="logout")
]