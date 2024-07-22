import utils as u       # file with all needed functions
from test_plate import json_event

### TEST 1: Check if we can add a plate to a database by posting it to the API, and if this database is updated.
###     PASS : A set plate that was not in the list is added (is in the list the second time it is checked)
###     FAIL : Either the plate was already in the list, the plate is not added correctly, or the plate is somehow removed

# This test is the exact same as TEST 2, just make sure here that the inout param is set to 0

url = u.CAMERA_URL+u.EXTENSION_EVENT

# Logic

response = u.requests.post(url, headers = u.HEADERS2, json=json_event)    # p.inout
response_def = u.json.loads(response.content) 

status = response_def['status']

print(response.status_code)
u.subtest(1, "POST", status, 0)

match status:
    case 0:
        u.print_test_result(1, True, "Plate posted succesfully", '')
    case 1:
        u.print_test_result(1, False, "Plate not posted", 'CODE 1: Client no permès')
    case 2:
        u.print_test_result(1, False, "Plate not posted", 'CODE 2: Falta el json, error de sintaxis del json')
    case 3:
        u.print_test_result(1, False, "Plate not posted", 'CODE 3: Operació desconeguda')
    case 4:
        u.print_test_result(1, False, "Plate not posted", 'CODE 4: Falta algun paràmetre al json')
    case 5:
        u.print_test_result(1, False, "Plate not posted", 'CODE 5: Error accedint a la BDD')
    case 6:
        u.print_test_result(1, False, "Plate not posted", 'CODE 6: Error intern desconegut')


