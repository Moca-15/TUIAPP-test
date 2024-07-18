### TEST TEMPLATES FOR CREATION, DO NOT EXECUTE

# set params from test_plate file
'''
import utils as u       # file with all needed functions
import test_plate as p

### TEST N: 
###     PASS : 
###     FAIL : 



# Logic
blue_list = u.get_blue_list()


# Results
success = False
status = ""
warning = ""

if   (p.plate):
    success = False
    status = ""
    warning = ""
elif (p.plate):
    success = False
    status = ""
    warning = ""
elif (p.plate):
    success = False 
    status = ""
    warning = ""
elif (p.plate):
    success = True
    status = ""


u.print_test_result(N, success, status, warning)

'''



# set params locally
'''
import utils as u       # file with all needed functions


### TEST N: 
###     PASS : 
###     FAIL : 

# Params
plate = '1023SWA'
created_at = u.PRESENT_TIME
filename = 'hhtps'
id_camera = '20'
inout = '0'             # 0 = in ; 1 = out


# Logic
blue_list = u.get_blue_list()


# Results
success = False
status = ""
warning = ""

if   (plate):
    success = False
    status = ""
    warning = ""
elif (plate):
    success = False
    status = ""
    warning = ""
elif (plate):
    success = False 
    status = ""
    warning = ""
elif (plate):
    success = True
    status = ""


u.print_test_result(N, success, status, warning)


'''

