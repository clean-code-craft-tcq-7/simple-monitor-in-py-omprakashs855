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

    def battery_type_threshold(self, battery_type, bms_obj):
        for battery in bms_obj.battery_type_mapping():
            if battery["Battery_Type"] == battery_type:
                return battery

def battery_is_ok(test_case):
    bms_obj = BMS()
    test_obj = Test_BMS()
    print("~"*len("Test Case : {}".format(test_case["Test_Case_Index"])))
    print("Test Case : {}".format(test_case["Test_Case_Index"]))
    print("~"*len("Test Case : {}".format(test_case["Test_Case_Index"])))
    threshold_dict_data = test_obj.battery_type_threshold(test_case["Battery_Type"], bms_obj)
    # adding extension 1 in these three check
    temp_result = temp_check(threshold_dict_data, test_case, bms_obj)
    soc_result = soc_check(threshold_dict_data, test_case, bms_obj)
    charge_rate_result = change_rate_check(threshold_dict_data, test_case, bms_obj)
    result = bool(temp_result * soc_result * charge_rate_result)
    # Printing Out of range values
    if not result:
        print_out_of_range_temp(bool(temp_result))
        print_out_of_range_soc(bool(soc_result))
        print_out_of_range_charge(bool(charge_rate_result))
    no_issue_check(result)
    return result