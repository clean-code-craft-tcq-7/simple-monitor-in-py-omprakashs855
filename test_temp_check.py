from Test_temp_type import temp_type

def temp_check(threshold_dict_data, test_case):
    # Convert temperature type to Celcius or Fahrenheit depending upon the battery threshold temperature type
    check_present = True
    temperature = test_case["Temperature"]
    if threshold_dict_data["Temp_Type"] != test_case["Temp_Type"]:
        temperature = temp_type(test_case["Temp_Type"], test_case["Temperature"])
    elif temperature < threshold_dict_data["Charge_Temp_Min"] or temperature > threshold_dict_data["Charge_Temp_Max"]:
        check_present = False
    return check_present

