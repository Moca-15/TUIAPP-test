import utils as u       # file with all needed functions
from test_plate import json_plates_no_phone, json_infractions, plate

### TEST 3:  Checks if the plate is expired, if it is check if it got an infraction
###     PASS : [The plate is inside its timeout & no infraction] or [The plate is not inside its timeout and an infraction has been posted (it's inside the infraction list)]  
###     FAIL : [The plate is inside its timeout & infraction] or [The plate is not inside its timeout and is not inside the infraction list]

url_plate = u.BASE_URL+u.EXTENSION_PLATE
url_infraction = u.BASE_URL+u.EXTENSION_INFRACTIONS


#### values needed:

# plate's remaining time

print("url_plate {} - headers {} - json {}".format(url_plate, u.HEADERS2, json_plates_no_phone))
response1 = u.requests.post(url_plate, headers = u.HEADERS2, json=json_plates_no_phone)
print("response1 status_code {} content {}".format(response1.status_code, response1.content))
response1_def = u.json.loads(response1.content)  
## the remaining time is negative

status_plate = response1_def["status"]
message = response1_def["message"]
try:
    time = response1_def["time"]
except:
    time = ""
    print("error posting database")
    print(message)

u.subtest(1, 'POST', status_plate, 0)


# wheter it got an infraction (need token!)
u.HEADERS1['Authorization'] = 'Bearer {}'.format(u.getToken(2))
response2 = u.requests.post(url_infraction, headers = u.HEADERS1, json=json_infractions)
response2_def = u.json.loads(response2.content)  

status_infractions = response2_def["status"]
message = response2_def["message"]
try:
    infractions = response2_def["infractions"]
except:
    infractions = ""
    print("error posting database")
    
u.subtest(2, 'POST', status_infractions, 0)



#### logic

success = False
st = ""
warning = ""

print(response2_def)
print (infractions)

plate_infracted = any(event['plate'] == plate for event in infractions)  #list comprehension returns true if plate is found in the infractions database

# request error 
if status_plate != 0 or status_infractions != 0:
    u.print_test_result(3, False, "There was a problem posting to source", f'plate status code = "{response1.status_code}"; intern status = "{status_plate}"\ninfraction status code = "{response2.status_code}"; intern status = "{status_infractions}"')
# plate inside timeout & no infraction
elif int(time) > 0 and plate_infracted == False:
    success = True
    st = "The plate is inside its timeout and doesn't have an infraction"
# plate inside timeout & infraction
elif int(time) > 0 and plate_infracted == True:
    success = False
    st = "The plate is inside its timeout but has an infraction"
# plate outside timeout & no infraction
elif int(time) <= 0 and plate_infracted == False:
    success = False
    st = "The plate is outside its timeout but doesn't have an infraction"
# plate outside timeout & no infraction
elif int(time) <= 0 and plate_infracted == True:
    success = True
    st = "The plate is outside its timeout and has an infraction"

u.print_test_result(3, success, st, warning)

