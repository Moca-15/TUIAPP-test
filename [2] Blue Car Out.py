import utils as u       # file with all needed functions
from test_plate import json_event

### TEST 2: Check if we can delete a plate from a database by posting it to the API with code out, and if this database is updated.
###     PASS : A set plate that was in the list is removed(is not in the list the second time it is checked)
###     FAIL : Either the plate was not in the list, the plate is not removed correctly, or the plate is somehow added

# This test is the exact same as TEST 1, just make sure here that the inout param is set to 1

url = u.CAMERA_URL+u.EXTENSION_EVENT

# Logic
response = u.requests.post(url, headers = u.HEADERS2, json=json_event)    # p.inout
response_def = u.json.loads(response.content) 

status = response_def['status']

print(response.status_code)
u.subtest(1, "POST", status, 0)

match status:
    case 0:
        u.print_test_result(2, True, "Plate removed succesfully", '')
    case 1:
        u.print_test_result(2, False, "Plate not removed", 'CODE 1: Client no permès')
    case 2:
        u.print_test_result(2, False, "Plate not removed", 'CODE 2: Falta el json, error de sintaxis del json')
    case 3:
        u.print_test_result(2, False, "Plate not removed", 'CODE 3: Operació desconeguda')
    case 4:
        u.print_test_result(2, False, "Plate not removed", 'CODE 4: Falta algun paràmetre al json')
    case 5:
        u.print_test_result(2, False, "Plate not removed", 'CODE 5: Error accedint a la BDD')
    case 6:
        u.print_test_result(2, False, "Plate not removed", 'CODE 6: Error intern desconegut')



