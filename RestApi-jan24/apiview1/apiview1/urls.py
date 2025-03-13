"""
URL configuration for apiview1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/', views.Employeeview.as_view()),
    path('listapi/', views.EmployeeListApiview.as_view()),
    path('createapi/', views.EmployeeCreateApiview.as_view()),
    path('retrieveapi/<int:pk>/', views.EmployeeRetrieveApiview.as_view()),
    path('updateapi/<int:pk>/', views.EmployeeUpdateApiview.as_view()),
    path('deleteapi/<int:pk>/', views.EmployeeDeleteApiview.as_view()),
    path('lcapi/', views.EmployeeListCreateApiview.as_view()),
     path('rudapi/<int:pk>/',views.EmployeeRetrieveUpdateDeleteApiview.as_view())


]
