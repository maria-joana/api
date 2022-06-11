from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.users import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
        ),
    path('users/', include(urls)),
]
