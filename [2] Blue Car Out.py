import utils as u       # file with all needed functions
import test_plate as p

### TEST 2: Check if we can delete a plate from a database by posting it to the API with code out, and if this database is updated.
###     PASS : A set plate that was in the list is removed(is not in the list the second time it is checked)
###     FAIL : Either the plate was not in the list, the plate is not removed correctly, or the plate is somehow added

# This test is the exact same as TEST 2, just make sure here that the inout param is set to 0

url = u.BASE_URL+u.EXTENSION_BLUE

# Logic
list, status_code = u.get_items(url)
before = u.list_plates(list)
u.subtest(1, "GET ", status_code)

u.post_item(url, p.plate, p.created_at, p.filename, p.id_camera, '1')    # p.inout
u.subtest(2, "POST", status_code)

list, status_code = u.get_items(url)
after = u.list_plates(list)
u.subtest(3, "GET ", status_code)


# Results
success = False
status = ""
warning = ""

if   (p.plate not in before) and (p.plate in after):
    success = False
    status = "A new plate was added to the database somehow"
elif (p.plate not in before) and (p.plate not in after):
    success = False
    status = "Unexisting plate not deleted from database"
    warning = "Expected the target plate to be inside the database"
elif (p.plate in before)     and (p.plate in after):
    success = False 
    status = "Plate was not deleted from database"
    warning = "Expected the value of inout of the test_plate to be 1, consider cheking"
elif (p.plate in before)     and (p.plate not in after):
    success = True
    status = "Plate was successfully deleted from database"


u.print_test_result(2, success, status, warning)