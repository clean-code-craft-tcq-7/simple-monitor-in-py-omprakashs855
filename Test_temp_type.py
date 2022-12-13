from BMS_Class import *

global bms_obj
bms_obj = BMS()

def temp_type(temp_type, temp):
    if temp_type == "Celcius":
        conv_result =  bms_obj.celcius_to_Fahr(temp)
    elif temp_type == "Fahrenheit":
        conv_result =  bms_obj.Fahr_to_celcius(temp)
    return conv_result