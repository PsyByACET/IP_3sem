from django.urls import path, include
from django.contrib import admin
from . import views
# from .views import taskView

app_name = "tasks"


urlpatterns = [
    path('', views.index, name=app_name),
    path('create', views.create, name='create'),
    path('dashboard', views.dashboard),
    path('list', views.list),
    path('users', views.usersView.as_view()),
    path('users/<int:pk>', views.usersView.as_view()),
    path('admin/', admin.site.urls),
    # path('tasks/<int:pk>', views.taskViewSet.as_view())
    path('tasks', views.taskViewSet),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register', views.register, name = 'register')
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]
