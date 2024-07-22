import utils as u       # file with all needed functions
import test_plate as p



url = u.BASE_URL+u.EXTENSION_PLATES+u.EXTENSION_ADD

# Logic

parameters = f'{{"id_zone":"1","id_user":3, "until":{p.time_until}, "plate":{p.plate}}}'
response = u.requests.post(url, headers = u.HEADERS1, data = parameters)    # p.inout
response_def = u.json.loads(response.content)  
status = response_def['status']
message = response_def['message']


u.subtest(1, "POST", status, 0)

match status:
    case 0:
        u.print_test_result(1, True, "Plate added succesfully", '')
    case 1:
        u.print_test_result(1, False, "Plate not added", f'CODE 1:{message}')
    case 2:
        u.print_test_result(1, False, "Plate not added", f'CODE 2: {message}')
    case 3:
        u.print_test_result(1, False, "Plate not added", f'CODE 3: {message}')



