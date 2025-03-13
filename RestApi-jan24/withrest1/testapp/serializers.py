from testapp.models import Employee
from rest_framework import serializers
#use modelserializer instead of naormal serializer work easy and less code
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'








# class EmployeeSerializer(serializers.Serializer):
#     eno=serializers.IntegerField()
#     ename=serializers.CharField(max_length=30)
#     esal=serializers.FloatField()
#     eaddr=serializers.CharField(max_length=30)
#     #object level validation for suuny and esal two validations
#     def validate(self,data):
#         ename=data.get('ename')
#         esal=data.get('esal')
#         if ename.lower()=='sunny':
#             if esal<50000:
#                 raise serializers.ValidationError("sunny  salaray should be minimum 50000....")
#         return data

#     # filed level validations
#     def validate_esal(self,value):
#         if value<5000:
#             raise serializers.ValidationError("Employee salaray should be minimum 5000....")
#         return value
#     #add for put method
#     def create(self,validated_data):
#         return Employee.objects.create(**validated_data)
#     def update(self,instance,validated_data):# instance =object and validated-data=pdict
#         instance.eno=validated_data.get('eno',instance.eno)
#         instance.ename=validated_data.get('ename',instance.ename)
#         instance.esal=validated_data.get('esal',instance.esal)
#         instance.eaddr=validated_data.get('eaddr',instance.eaddr)
#         instance.save()
#         return instance




