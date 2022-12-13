import os
import sys
from test_temp_check import temp_check
from test_charge_rate_check import change_rate_check
from test_soc_check import soc_check
from print_test_case_result import *
from BMS_Class import *

class Test_BMS:

    def temp_type_check(self, temp_type, test_temp_type):
        check_same = False
        if temp_type == test_temp_type:
            check_same = True
        return check_same

    def battery_type_threshold(self, battery_type):
        bms_obj = BMS()
        for battery in bms_obj.battery_type_mapping():
            if battery["Battery_Type"] == battery_type:
                return battery

def battery_is_ok(test_case):
    test_obj = Test_BMS()
    threshold_dict_data = test_obj.battery_type_threshold(test_case["Battery_Type"])
    temp_result = temp_check(threshold_dict_data, test_case)
    soc_result = soc_check(threshold_dict_data, test_case)
    charge_rate_result = change_rate_check(threshold_dict_data, test_case)
    result = temp_result and soc_result and charge_rate_result
    # Printing Out of range values
    if not result:
        print_test_case(test_case)
        print_out_of_range_temp(temp_result)
        print_out_of_range_soc(soc_result)
        print_out_of_range_charge(charge_rate_result)
    return result

