import utils as u       # file with all needed functions
import test_plate as p

### TEST 3:  Checks if the plate is expired, if it is issueaas an infraction (posts an infraction to the black list with automatic tag)
###     PASS : [The plate is inside its timeout] or [The plate is not inside its timeout and an infraction has been posted (it's inside the infraction list)]  
###     FAIL : [The plate is not inside its timeout and is not inside the infraction list]

url = u.BASE_URL+u.EXTENSION_BLUE
url_black = u.BASE_URL+u.EXTENSION_BLACK

# Logic
time_in      = ""
past_time    = ""
current_time = ""
timeout_time = ""

success = False

list, status_code = u.get_items(url)
u.subtest(1, "GET ", status_code)

for i in list:
    if i['License'] == p.plate:
        time_in = i['created_at']     
        past_time, current_time, timeout_time = u.calc_timeout(time_in)
        
    # true if car needs infraction and it posted successfully
        if current_time >= timeout_time:
            status_code, exists = u.check_infraction(url_black, i['License'])   
            u.subtest(2, "GET ", status_code)
            if exists == 1:
                success = True
            break   # no need to keep running if we found the one
        elif current_time < timeout_time:
            status_code, exists = u.check_infraction(url_black, i['License'])   
            u.subtest(2, "GET ", status_code)
            if exists == 0:         # there should not be an infraction 
                success = True
        

# Results
status = ""
warning = ""

if   time_in == "":
    status = "No such plate in database"
elif current_time >= timeout_time and success == False:
    status = "Plate has expired, but infraction not posted"
    warning = "Plate " + p.plate + " added at " + time_in + " is in database has surpassed its threshold time at " + timeout_time.strftime("%Y-%m-%d %H:%M:%S")
elif current_time >= timeout_time and success == True:
    status = "Plate has expired, and infraction posted successfully"
    warning = "Plate " + p.plate + " added at " + time_in + " is in database has surpassed its threshold time at " + timeout_time.strftime("%Y-%m-%d %H:%M:%S") + (", and was added to the black list")
elif current_time < timeout_time and success == False:
    status = "Plate is inside its time limit, but infraction posted"
    warning = "Plate " + p.plate + " added at " + time_in + " is in database has not surpassed its threshold time at " + timeout_time.strftime("%Y-%m-%d %H:%M:%S" + " but there exists an infraction for this license")
elif current_time < timeout_time and success == True:
    status = "Plate is inside its time limit, infraction not posted"
    warning = "Plate " + p.plate + " added at " + time_in + " is in database has not surpassed its threshold time at " + timeout_time.strftime("%Y-%m-%d %H:%M:%S")


u.print_test_result(3, success, status, warning)