from django.urls import path
from octavius import views

urlpatterns = [
    path('sleep/', views.sleep),
    path('sleep/<int:pk>/', views.sleep_update),
]