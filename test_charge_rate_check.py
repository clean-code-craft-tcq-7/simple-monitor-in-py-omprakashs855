from print_test_case_result import *

def change_rate_check(threshold_dict_data, test_case, bms_obj):
    check_present = 1
    if test_case["Charge_rate"] > threshold_dict_data["Charge_rate"]:
        check_present = 0
    else:
        print_tolerence_min(bms_obj.tolerance_check_min(threshold_dict_data["Charge_rate"], test_case["Charge_rate"]), "min charge-rate")
        print_tolerence_max(bms_obj.tolerance_check_min(threshold_dict_data["Charge_rate"], test_case["Charge_rate"]), "max charge-rate")
    return check_present