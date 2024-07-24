import utils as u


url = u.BASE_URL+u.EXTENSION_ZONE+'/1'
# 1: blue
# 2: orange
# 3: green



response, status_code = u.get_items(url, u.HEADERS1)

print(status_code)
print(response)

'''

status = response['status']
message = response['message']
plates = ''

if status == 0:
    plates = response['plates']


for plate in plates:
    print(plates)


match status:
    case 0:
        u.print_test_result(0, True, "GET plates succesful", f'token={bearer_token}')
    case 1:
        u.print_test_result(0, False, "GET plates error", f'STATUS 1:{message}')
    case 2:
        u.print_test_result(0, False, "GET plates error", f'STATUS 2:{message}')
'''