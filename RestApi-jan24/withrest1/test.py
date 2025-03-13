import requests,json
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'
#object level validation 
# if ename=sunny then salaray is  min 50000
def  updated_resource(id):
    data={
        'id':id,
        'ename':'Sunny',
        'esal':5003
    }
    resp = requests.put(BASE_URL + END_POINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
updated_resource(1)



# # validation for filed level
# def  updated_resource(id):
#     data={
#         'id':id,
#         'esal':5002
#     }
#     resp = requests.put(BASE_URL + END_POINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# updated_resource(4)

# def delete_resource(id):
#     data={
#         'id':id
#     }
#     resp = requests.delete(BASE_URL + END_POINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# delete_resource(7)



# def update_resource(id):
#     new_emp = {
#     'id':id,
#     'esal':16000.600,
#     'eaddr':'guntur'
#     }
#     resp = requests.put(BASE_URL + END_POINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# update_resource(1)  


# def create_resource():
#     new_emp = {
#     'eno':105,
#     'ename':'Radhika',
#     'esal':19000,
#     'eaddr':'Delhi'
#     }
#     resp = requests.post(BASE_URL + END_POINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# create_resource()  


# def get_resource(id = None):
#     data = {}
#     if id is not None:
#         data ={
#         'id':id
#         }
#     resp = requests.get(BASE_URL + END_POINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# get_resource(2)