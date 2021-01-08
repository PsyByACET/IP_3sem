from django.urls import path
from . import views
# from .views import taskView

app_name = "users"

urlpatterns = [
    path('', views.index, name='main'),
    path('about', views.about),
    path('create', views.create, name='create'),
    path('users', views.usersView.as_view()),
    path('users/<int:pk>', views.usersView.as_view())
]
