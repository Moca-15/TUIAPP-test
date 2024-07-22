import utils as u       # file with all needed functions
import test_plate as p



url = u.BASE_URL+u.EXTENSION_INFRACTIONS

# Logic

parameters = f'{{"id_zone":1, "from":{p.time_from}, "to":{p.time_until}}}'

response = u.requests.get(url, headers = u.HEADERS1, data = parameters)    # p.inout
response_def = u.json.loads(response.content)  

status = response_def['status']
message = response_def['message']

u.subtest(1, "POST", status, 0)  

match status:
    case 0:
        infractions = response_def['infractions']
        for i in infractions:
            print(i)
        u.print_test_result(1, True, "Infractions consulted successfully", '')
    case 1:
        u.print_test_result(1, False, "Infractions not consulted", f'CODE 1:{message}')
    case 2:
        u.print_test_result(1, False, "Infractions not consulted", f'CODE 2: {message}')
