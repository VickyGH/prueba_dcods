from django.urls import path, include
from .views import *

urlpatterns = [
    path('registration/', include('rest_registration.api.urls')),
    # Registration
    path('register/', RegisterUserProfileViewSet.as_view(), name="register_user"),
    path('activate/', ActivateUserProfileViewSet, name="register_user"),
    path('get/user/', GetUserData.as_view(), name="user_data"),



]
