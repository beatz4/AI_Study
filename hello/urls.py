from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    # 1 - path, 2 - function, 3 - second parameter
    path("hello/<name>", views.hello_there, name="hello_there"),
]