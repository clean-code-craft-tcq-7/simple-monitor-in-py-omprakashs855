from Test_BMS_Class import *

TEST_CASE_1 = {
                "Battery_Type" : "Li-ion",
                "Temp_Type" : "Fahrenheit",
                "Temperature" : 68,
                "SOC" : 70,
                "Charge_rate" : 0.7
            }

TEST_CASE_2 = {  
                "Battery_Type" : "Li-ion",
                "Temp_Type" : "Celcius",
                "Temperature" : 50,
                "SOC" : 85,
                "Charge_rate" : 0
            }

if __name__ == '__main__':
  assert(battery_is_ok(TEST_CASE_1) is True)
  assert(battery_is_ok(TEST_CASE_2) is False)
