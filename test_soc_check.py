from print_test_case_result import *

def soc_check(threshold_dict_data, test_case, bms_obj):
    check_present = 1
    if test_case["SOC"] < threshold_dict_data["SOC_min"] or test_case["SOC"] > threshold_dict_data["SOC_max"]:
        check_present = 0
    else:
        print_tolerence_min(bms_obj.tolerance_check_min(threshold_dict_data["SOC_min"], test_case["SOC"]), "discharging")
        print_tolerence_max(bms_obj.tolerance_check_max(threshold_dict_data["SOC_max"], test_case["SOC"]), "charge-peak")
    return check_present