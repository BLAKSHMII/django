
from django.urls import path
from testapp3 import views
urlpatterns = [
    path('hyd/', views.hyd_jobs),
    path('vij/', views.vij_jobs),
    path('gun/',views.gun_jobs),
]
