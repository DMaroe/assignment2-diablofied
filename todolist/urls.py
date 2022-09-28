from django.urls import path
from todolist.views import  delete, register, login_user, logout_user, show_todos, new_task, refresh

app_name = "todolist"

#routing url 
urlpatterns = [
    path('', show_todos, name='show_todos'),
    path('login/', login_user, name='login_user'),
    path('register/', register, name='register'),
    path('create-task/', new_task, name='new_task'),
    path('logout/', logout_user, name='logout_user'),
    path('refresh/<str:id>/', refresh, name="refresh"),
    path('delete/<str:id>/', delete, name="delete")
]