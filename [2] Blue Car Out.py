import utils as u       # file with all needed functions
import test_plate as p

### TEST 2: Check if we can delete a plate from a database by posting it to the API with code out, and if this database is updated.
###     PASS : A set plate that was in the list is removed(is not in the list the second time it is checked)
###     FAIL : Either the plate was not in the list, the plate is not removed correctly, or the plate is somehow added

# This test is the exact same as TEST 1, just make sure here that the inout param is set to 1

url = u.BASE_URL+u.EXTENSION_EVENT

# Logic
response, status_code = u.post_item(url, u.HEADERS2, p.detected_at, p.plate, p.filename, p.id_camera, '0')    # p.inout
status = response['status']

u.subtest(2, "POST", status, 0)

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



