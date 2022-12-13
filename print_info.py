from print_test_case_result import *

def print_info_all(test_case, temp_result, soc_result, charge_rate_result):
    result = temp_result and soc_result and charge_rate_result
    if not result:
        print_test_case(test_case)
        print_out_of_range_temp(temp_result)
        print_out_of_range_soc(soc_result)
        print_out_of_range_charge(charge_rate_result)