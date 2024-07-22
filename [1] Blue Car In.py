import utils as u       # file with all needed functions
import test_plate as p

### TEST 1: Check if we can add a plate to a database by posting it to the API, and if this database is updated.
###     PASS : A set plate that was not in the list is added (is in the list the second time it is checked)
###     FAIL : Either the plate was already in the list, the plate is not added correctly, or the plate is somehow removed

# This test is the exact same as TEST 2, just make sure here that the inout param is set to 0

url = u.BASE_URL+u.EXTENSION_EVENT

# Logic

response, status_code = u.post_item(url, u.HEADERS2, p.detected_at, p.plate, p.filename, p.id_camera, '0')    # p.inout
status = response['status']

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



