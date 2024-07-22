import utils as u       # file with all needed functions
from test_user import json_user


url = u.BASE_URL + u.EXTENSION_LOGIN

response = u.requests.post(url, headers=u.HEADERS2, json=json_user)
print(response)
response_def = u.json.loads(response.content)  
print(response_def)

status = response_def["status"]
message = response_def["message"]


#print(response_def)

u.subtest(0, 'POST', status, 0)

token = ''
id_user = ''
name = ''

if status == 0:
    token = response_def['token']
    id_user = response_def['id_user']
    name = response_def['name']


match status:
    case 0:
        u.print_test_result(0, True, "Login succesful", f'token={token}; id_user={id_user}; name={name}')
    case 1:
        u.print_test_result(0, False, "Login error", f'STATUS 1:{message}')
    case 2:
        u.print_test_result(0, False, "Login error", f'STATUS 2:{message}')
    case 3:
        u.print_test_result(0, False, "Login error", f'STATUS 3:{message}')

