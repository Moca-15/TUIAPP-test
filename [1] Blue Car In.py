import utils as u       # file with all needed functions
import test_plate as p

### TEST 1: Check if we can add a plate to a database by posting it to the API, and if this database is updated.
###     PASS : A set plate that was not in the list is added (is in the list the second time it is checked)
###     FAIL : Either the plate was already in the list, the plate is not added correctly, or the plate is somehow removed

# This test is the exact same as TEST 2, just make sure here that the inout param is set to 0

url = u.BASE_URL+u.EXTENSION_BLUE

# Logic
list, status_code = u.get_items(url)
before = u.list_plates(list)
u.subtest(1, "GET ", status_code)

u.post_item(url, p.plate, p.created_at, p.filename, p.id_camera, '0')    # p.inout
u.subtest(2, "POST", status_code)

list, status_code = u.get_items(url)
after = u.list_plates(list)
u.subtest(3, "GET ", status_code)


# Results
success = False
status = ""
warning = ""


if   (p.plate not in before) and (p.plate in after):
    success = True
    status = "New plate added to the database"
elif (p.plate not in before) and (p.plate not in after):
    success = False
    status = "New plate not added to database"
    warning = "Expected the value of inout of the test_plate to be 0, consider cheking"
elif (p.plate in before)     and (p.plate in after):
    success = False 
    status = "New plate already in database"
    warning = "Run Test for duplicate elements check"
elif (p.plate in before)     and (p.plate not in after):
    success = False
    status = "Idk how can this even happen"
    warning = "please check the inout parameter, should equal 0 for this case"


u.print_test_result(1, success, status, warning)