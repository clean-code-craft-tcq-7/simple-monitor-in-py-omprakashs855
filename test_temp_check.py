from print_test_case_result import *

def temp_check(threshold_dict_data, test_case, bms_obj):

    # Convert temperature type to Celcius or Fahrenheit depending upon the battery threshold temperature type
    check_present = 1
    temperature = bms_obj.temp_type_check(threshold_dict_data, test_case)
    if temperature < threshold_dict_data["Charge_Temp_Min"] or temperature > threshold_dict_data["Charge_Temp_Max"]:
        check_present = 0
    else:
        print_tolerence_min(bms_obj.tolerance_check_min(threshold_dict_data["Charge_Temp_Min"], threshold_dict_data["Charge_Temp_Max"], temperature), "min temperature")
        print_tolerence_max(bms_obj.tolerance_check_max(threshold_dict_data["Charge_Temp_Max"], temperature), "max temperature")
    return check_present

