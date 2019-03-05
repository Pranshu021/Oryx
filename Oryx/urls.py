from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'oryx'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name="index"),
    path('signup/', include('signup.urls'), name="signup"),
    path('login/', include('login.urls'), name="login"),
    path('profile/', include('profiles.urls'), name="profile"),
    path('home/', include('home.urls'), name="home"),
    path('products/', include('productapi.urls'), name="products"),
    path('logout/', views.LogoutView, name="logout"),
    path('test/', views.TestView, name="test"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('contact-us', views.ContactView.as_view(), name="contact"),
    path('testing', views.TestView, name="test"),
    path('api/', include('api.urls'), name="api"),
    path('privacy_policy', views.PrivacyPolicy, name="privacy_policy"),
    path('upload', views.UploadView, name="upload"),
] 
