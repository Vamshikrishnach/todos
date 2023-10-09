from django.urls import path, include
from rest_framework import routers
from todosapp.views import *

app_name = "todosapp"

urlpatterns = [
    path('task1',Task1ListView.as_view(),name='task1'),
    path('task1/<int:pk>',Task1CRUD.as_view(),name='task1'),
    path('taskcompletion',TaskCompletionList,name='taskcompletion'),
    path('taskcompletion/<int:pk>',TaskCompletionView,name='taskcompletion'),
    path('taskcreator/<int:pk>/', TaskCreatorDetailView.as_view(), name='taskcreator-detail'),
    
]
