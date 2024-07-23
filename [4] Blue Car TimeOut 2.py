import utils as u       # file with all needed functions
from test_plate import json_plates_no_phone, json_infractions, plate

### TEST 4: Check if the plate whith an infraction has been removed from the blue list and added to the black list
###     PASS : Infracted plate not in Blue, in Black
###     FAIL : Infracted plate in Blue // Infracted plate not in BLack

url_plate = u.BASE_URL+u.EXTENSION_PLATE
url_infraction = u.BASE_URL+u.EXTENSION_INFRACTIONS

# Logic

#### values needed:

# plate's remaining time

print("url_plate {} - headers {} - json {}".format(url_plate, u.HEADERS2, json_plates_no_phone))
response1 = u.requests.post(url_plate, headers = u.HEADERS2, json=json_plates_no_phone)
print("response1 status_code {} content {}".format(response1.status_code, response1.content))
response1_def = u.json.loads(response1.content)  
# em sembla que ara peta perquè retorna un json buit o en un altre fromat i no es pot decodificar bé

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
