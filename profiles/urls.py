from django.urls import path
from . import views

app_name = "profile"

urlpatterns = [
    path('<str:username>', views.ProfileView, name="profile"),
    path('users/<str:user_search>', views.UserProfileViews, name="users"),
    path('settings/change_password', views.ChangePasswordView, name="change_password"),
]
