from django.urls import path
from . import views

app_name = 'Login'
urlpatterns = [

    path('', views.ClassIndex.as_view(), name="index"),
    path('login/', views.LoginClass.as_view(), name="login"),
    path('view-user/', views.ViewUser.as_view(), name="user_view"),
    path('view-product/', views.view_product,name='view_product'),
]
