### IMPORTS

# això és perquè d'alguna manera se m'ha instal·lat malament on no toca la llibreria de requests, si algú sap com solucionar-ho i em pot ajudar m'aniria bé perquè porto +4h només amb això 
import sys      # i sé que aquesta solució és un nyap com una casa però funciona.
sys.path.append("C:\Python312\Lib\site-packages")
# si et funciona la llibreria, comenta aquestes dues línies abans d'executar


import requests
import json

from datetime import datetime, timezone, timedelta

import traceback
from time import gmtime

### CONSTANTS 

# BEARER_TOKEN = ""
CAMERA_URL = 'http://vpn.aurora2.vibracom.eu/tui'
BASE_URL   = 'https://api.aurora2.vibracom.eu/tui'
EXTENSION_EVENT = '/event'
EXTENSION_LOGIN = '/login'
EXTENSION_ZONE = '/zone'
EXTENSION_PLATES = '/plates'
EXTENSION_PLATE = '/plate'
EXTENSION_ADD = '/add'
EXTENSION_DEL = '/delete'
EXTENSION_INFRACTIONS = '/infractions' 

bearer_token = ''
HEADERS1 = {
    'Authorization': f'Bearer {bearer_token}',
    'Content-Type': 'application/json'
}

HEADERS2 = {
    'Content-Type': 'application/json'
}

PRESENT_TIME = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
TIMEOUT = 3600      # in second


### FANCY FUNCTIONS
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def print_test_result(test_num, success, status, warning):
    print('\n\t' + color.BOLD + 'TEST ' + str(test_num) + color.END, end= '  ')
    if success == True:
        print(color.GREEN + 'PASS' + color.END)
    else:
        print(color.RED + 'FAIL' + color.END)
    print(status)
    if warning != '':
        print(color.YELLOW + warning + color.END)
    print("\n")

def subtest(query_num, query_type, status_code, correct_status):
    print(str(query_num) + ' ' + query_type + "   Status code: " + str(status_code), end=" ")
    if status_code == correct_status:
        print(color.GREEN + "OK" + color.END)
    else:
        print(color.RED + "NOK" + color.END)



### GENERAL TEST FUNCTIONS

## QUERIES

def get_items(url, header):
    list = requests.get(url, headers = header)                  # sends the GET request
    list_items = json.loads(list.content)                       # deserialize json instance to a python object blue_list,
    return list_items, list.status_code                         # we get the deserialization of a json object that contains the llist of elements in the blue database



def post_item(url, headers, detected_at, plate, filename, id_camera, inout):
    parameters = f'detected_at={str(detected_at)}&plate={plate}&filename={filename}&id_camera={id_camera}&inout={inout}'
    response = requests.post(url, headers = headers, data = parameters)
    return json.loads(response.content), response.status_code
    # print(get)            # should be none or null bc the POST request just sends data, not receives  


## OTHER


# create a list to save only the plate values
def list_plates(items):
    plates = [item['License'] for item in items]         
    return plates 




# returns 3 datetime objects
def calc_timeout(time_in):
    # these are not strings, these are all datetime vars 
    past_time    = datetime.strptime(time_in, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc) # convert 'current_time'(string) to datetime type
    current_time = datetime.strptime(PRESENT_TIME, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)  # convert PRESENT_TIME(string) to datetime type
    # the threshold time, when the permission expires
    timeout_time = past_time + timedelta(seconds=TIMEOUT)
    return past_time, current_time, timeout_time
# use .strftime("%Y-%m-%d %H:%M:%S") to turn to stings

# check if the infraction was issued. return bool
def check_infraction(url, plate, past_time, timeout_time, current_time):
    list, status_code = get_items(url)
    for i in list:
        if (i['License'] == plate) and i['agent_id'] == '0':
            return status_code, 1
    return status_code, 0


# get token

def getTokenApi(user, password, url="https://api.aurora2.vibracom.eu/tui/login"):
    addLog("=> getToken")
    json = {"user":user, "password":password}
    addLog("Will send {} to {}".format(json, url))
    try:
        response = requests.post(url, json=json)
        addLog("Code: {} - response: {}".format(response.status_code, response.content))
        if response.status_code != 200:
            addLog("ERROR")
            addLog("<= getToken 1")
            return False
        addLog("<= getToken 2")
        return response.json()        
    except Exception as e:
        addLog("Error: {}".format(e))
        addLog(traceback.format_exc())
        addLog("<= getToken 3")
        return False    
    
def GetPrettyStrDateTime():
    currDateTime = gmtime()
    return "{}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(currDateTime[0], currDateTime[1], currDateTime[2], currDateTime[3], currDateTime[4], currDateTime[5])

def addLog(logstr, showTime=True, endSymbol="\n"):
    if showTime:
        iniLogStr = "{} > ".format(GetPrettyStrDateTime())
    else:
        iniLogStr = ""
    print(iniLogStr, end="")
    print(logstr.strip(), end=endSymbol)  
    with open("./trace.log", 'a') as file: 
            file.write(iniLogStr + logstr.strip() + endSymbol)  

def getToken(userType = 0):

    # users: 0 -> ajuntament, 1 -> veï, 2 -> policia
    users = [["user1", "password1"], ["user3", "password3"],["agent1", "password5"]]

    response = getTokenApi(users[userType][0], users[userType][1])
    assert(response != False)
    assert("token" in response)
    return response["token"]
