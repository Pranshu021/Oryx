from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'api'

urlpatterns = [
    path('smartphoneapi/<str:name>', views.SmartphoneAPIView.as_view(), name="smartphoneAPI"),
] 
