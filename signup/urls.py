from django.urls import path
from . import views

app_name = 'signup'

urlpatterns = [
    path('', views.SignUpView.as_view(), name="signup")
]