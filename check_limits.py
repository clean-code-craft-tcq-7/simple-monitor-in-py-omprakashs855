from Test_BMS_Class import *
import json

if __name__ == '__main__':
  with open('test_case.json', 'r') as jsonread:
    test_case_data = json.load(jsonread)
  
  for test_case in test_case_data["TEST_CASE"]:
    assert(battery_is_ok(test_case) is test_case["assert_check"])
