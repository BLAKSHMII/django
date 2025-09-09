from django.urls import path
from testapp import views
urlpatterns = [
    path('first/', views.firstview),
    path('second/', views.secondview),
    path('third/', views.thirdview),
]
