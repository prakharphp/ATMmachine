from django.urls import path, include

from . import views

urlpatterns = [
    path('users/', views.ListTodo.as_view()),
    path('users/<int:pk>/', views.DetailTodo.as_view()),
    path('users/deposit/<int:card>/<int:amount>', views.deposit),
    path('users/withdraw/<int:card>/<int:amount>', views.withdraw),
    path('rest-auth/', include('rest_auth.urls')),
]
