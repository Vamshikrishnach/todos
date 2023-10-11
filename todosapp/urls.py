from django.urls import path, include
from rest_framework import routers
from todosapp.views import *

app_name = "todosapp"

signup_router = routers.SimpleRouter()
signup_router.register('signup', UserSiginUpViewset, basename='signup') 

signin_router = routers.SimpleRouter()
signin_router.register('signin', UserSignInViewset, basename='signin') 

forgotpassword_router = routers.SimpleRouter()
forgotpassword_router.register('forgotpassword', ForgetpasswordViewSet, basename='forgotpassword') 

forgotpasswordVerify_router = routers.SimpleRouter()
forgotpasswordVerify_router.register('forgotpasswordVerify', ForgetpasswordVerifyViewSet, basename='forgotpasswordVerify') 


urlpatterns = [
    path('',include(signup_router.urls)),
    path('',include(signin_router.urls)),
    path('',include(forgotpassword_router.urls)),
    path('',include(forgotpasswordVerify_router.urls)),
    path('task1',Task1ListView.as_view(),name='task1'),
    path('task1/<int:pk>',Task1CRUD.as_view(),name='task1'),
    path('taskcompletion',TaskCompletionList,name='taskcompletion'),
    path('taskcompletion/<int:pk>',TaskCompletionView,name='taskcompletion'),
    path('taskcreator/<int:pk>/', TaskCreatorDetailView.as_view(), name='taskcreator-detail'),
    
]
