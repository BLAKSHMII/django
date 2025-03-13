from django.urls import path,include
from rest_framework.routers import DefaultRouter
from testapp.api.views import EmployeeCRUDview
router=DefaultRouter()
router.register('empview',EmployeeCRUDview)
urlpatterns=[
    path('',include(router.urls))
]
