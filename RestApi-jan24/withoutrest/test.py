import requests
BASE_URL='http://127.0.0.1:8000/'
END_POINT="jsoncbv/"
resp=requests.put(BASE_URL+END_POINT)  #get method access data
print(type(resp))
print(resp)
print(type(resp.json()))
print(resp.json())
data=resp.json()
print(data)
# print("-"*30)
# print(data['eno'])
# print(data['ename'])
# print(data['esal'])
# print(data['eaddr'])