from rest_framework.viewsets import ModelViewSet
from testapp.models import Employee
from testapp.api.serializers import EmployeeSerializer
class EmployeeCRUDview(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer