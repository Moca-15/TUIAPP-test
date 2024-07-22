from utils import PRESENT_TIME

# Set parameters of the Test Plate. some tests do not use all parameters
detected_at = PRESENT_TIME
plate = '1023CCC'
filename = 'hhtps'
id_camera = '20'
zone = 'azul'
inout = '1'             # 0 = in ; 1 = out


time_from = "2024-07-10 00:00:00" 
time_until = "2024-07-15 18:00:00"

phone = ""
notify = ""


json_event = {
    'detected_at': detected_at,
    'plate': plate,
    'filename': filename,
    'id_camera': id_camera,
    'inout': inout
}

json_plates ={
    'plate': plate,
    'phone': phone,
    'notify': notify
}

json_infractions = {
    'id_zone': zone,
    'from': time_from,
    'to': time_until
}

