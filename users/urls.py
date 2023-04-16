from django.urls import path, include
from .views import UsersAPIView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UsersAPIView, MyTokenObtainPairView

urlpatterns = [
    path('', UsersAPIView.as_view()), # this means any request to root of the server are mapped to UserAPIView
    path('login/', MyTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]