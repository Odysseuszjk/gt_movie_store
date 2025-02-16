from django.urls import path
from . import views
from .views import health_check
urlpatterns = [
    path('', views.index, name='home.index'),
    path('about', views.about, name='home.about'),
    path("kaithhealthcheck", health_check, name="health_check"),  # ✅ Add Health Check URL
]
