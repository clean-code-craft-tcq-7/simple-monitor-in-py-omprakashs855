def temp_check(threshold_dict_data, test_case):
    # Convert temperature type to Celcius or Fahrenheit depending upon the battery threshold temperature type
    check_present = True
    temperature = test_case["Temperature"]
    if temperature < threshold_dict_data["Charge_Temp_Min"] or temperature > threshold_dict_data["Charge_Temp_Max"]:
        check_present = False
    return check_present

