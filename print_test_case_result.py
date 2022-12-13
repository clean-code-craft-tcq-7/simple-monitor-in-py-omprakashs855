
def print_test_case(test_case):
    print("Battery_Type : {}".format(test_case["Battery_Type"]))
    print("Temperature : {}".format(test_case["Temperature"]))
    print("SOC : {}".format(test_case["SOC"]))
    print("Charge_rate : {}".format(test_case["Charge_rate"]))

def print_out_of_range_temp(check_flag):
    if not check_flag:
        print('Temperature is out of range!')

def print_out_of_range_soc(check_flag):
    if not check_flag:
        print('State of Charge is out of range!')

def print_out_of_range_charge(check_flag):
    if not check_flag:
        print('Charge rate is out of range!')

def print_info(test_case, temp_result, soc_result, charge_rate_result):
    result = temp_result and soc_result and charge_rate_result
    if not result:
        print_test_case(test_case)
        print_out_of_range_temp(temp_result)
        print_out_of_range_soc(soc_result)
        print_out_of_range_charge(charge_rate_result)