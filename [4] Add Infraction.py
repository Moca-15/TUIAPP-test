import utils as u       # file with all needed functions
import test_plate as p
import time
### TEST 4: Checks the database periodically to see if some plate has expired
###     PASS : For a set time, check all the plates within the database & issue an infraction when needed
###     FAIL : The required infractions were not issued or posted correctly, etc

# In progress

url = u.BASE_URL+u.EXTENSION_BLUE

# Logic
t = 30              # will check the db every 30 seconds
duration = 3600     # will check the db for 1h
n_fetches = 0

while duration > 0:
    time.sleep(t)
    list = u.get_items(url)        # fetch the db
    n_fetches =+ 1
    for item in list:
        past_time, current_time, timeout_time = u.calc_timeout(item['created_at'])
        if current_time >= timeout_time:
            print("Plate " + item['License'] + " added at " + item['created_at'] + " is in database blue has surpassed its threshold time at " + timeout_time.strftime("%Y-%m-%d %H:%M:%S"))
            if u.issue_infraction() == False: # infraction went wrong
                u.print_test_result(4, False, "Automatic Infraction not posted", "")
            else:
                u.print_test_result(4, True, "Automatic Infraction posted successfully", "")
        else:
            continue
    duration =- t

print("number of fetches to database: ", n_fetches)