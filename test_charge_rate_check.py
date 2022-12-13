
def change_rate_check(threshold_dict_data, test_case):
    check_present = True
    if test_case["Charge_rate"] > threshold_dict_data["Charge_rate"]:
        check_present = False
    return check_present