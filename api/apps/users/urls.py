from django.urls import path
from .views import RegisterUserView, ListUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('list/', ListUserView.as_view(), name='list'),
]
