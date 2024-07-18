### IMPORTS

# això és perquè d'alguna manera se m'ha instal·lat malament on no toca la llibreria de requests, si algú sap com solucionar-ho i em pot ajudar m'aniria bé perquè porto +4h només amb això 
import sys      # i sé que aquesta solució és un nyap com una casa però funciona.
sys.path.append("C:\Python312\Lib\site-packages")
# si et funciona la llibreria, comenta aquestes dues línies abans d'executar


import requests
import json

from datetime import datetime, timezone, timedelta

### CONSTANTS 

BASE_URL = 'https://c60d32ofo0.execute-api.eu-central-1.amazonaws.com'
EXTENSION_BLUE = '/BlueList?'
EXTENSION_BLACK =''


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

def subtest(query_num, query_type, status_code):
    print(str(query_num) + ' ' + query_type + "   Status code: " + str(status_code), end=" ")
    if status_code == 200:
        print(color.GREEN + "OK" + color.END)
    else:
        print(color.RED + "NOK" + color.END)



### GENERAL TEST FUNCTIONS

## QUERIES

def get_items(url):
    list = requests.get(url)                    # sends the GET request
    blue_items = json.loads(list.content)       # deserialize json instance to a python object blue_list,
    return blue_items, list.status_code                           #  we get the deserialization of a json object that contains the llist of elements in the blue database



def post_item(url, plate, created_at, filename, id_camera, inout):
    parameters = 'plate='+plate+'&created_at='+str(created_at)+'&filename='+filename+'&id_camera='+id_camera+'&inout='+inout
    return requests.post(url+parameters)
    # response = requests.post(BASE_URL+EXTENSION_BLUE+parameters)  # not really necesary to assign to a variable
    # get = response.json()
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


