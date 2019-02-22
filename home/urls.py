from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name="home"

urlpatterns = [
    path('', login_required(views.HomeView.as_view(), login_url='login:login'), name="home"),
]
