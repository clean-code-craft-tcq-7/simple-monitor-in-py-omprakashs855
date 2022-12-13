
def soc_check(threshold_dict_data, test_case):
    check_present = 1
    if test_case["SOC"] < threshold_dict_data["SOC_min"] or test_case["SOC"] > threshold_dict_data["SOC_max"]:
        check_present = 0
    return check_present