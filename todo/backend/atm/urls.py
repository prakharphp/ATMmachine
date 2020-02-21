from django.urls import path, include

from . import views

urlpatterns = [
    path('users/', views.ListTodo.as_view()),
    path('users/<int:pk>/', views.DetailTodo.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
]
