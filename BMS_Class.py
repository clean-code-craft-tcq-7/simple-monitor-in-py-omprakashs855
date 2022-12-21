class BMS:
        
    def battery_type_mapping(self):
        # This method is used to store BMS 
        # info regarding multiple battery type

        battery_bms_info = [
            {
                "Battery_Type" : "Li-ion",
                "Temp_Type" : "Celcius",
                # Charging
                "Charge_Temp_Min" : 0,
                "Charge_Temp_Max" : 45,
                # Discharging, not used yet
                "Discharge_Temp_Min" : -20,
                "Discharge_Temp_Max" : 65,
                "SOC_min" : 20,
                "SOC_max" : 80,
                "Charge_rate_max": 0.8,
                "Charge_rate_min": 0
            }
        ]
        return battery_bms_info
    
    def temp_type_check(self, threshold_dict_data, test_case):
        temperature = test_case["Temperature"]
        if threshold_dict_data["Temp_Type"] != test_case["Temp_Type"]:
            temperature = self.temp_type(test_case["Temp_Type"], test_case["Temperature"])
        return temperature

    def temp_type(self, temp_type, temp):
        if temp_type == "Celcius":
            conv_result =  self.celcius_to_Fahr(temp)
        elif temp_type == "Fahrenheit":
            conv_result =  self.Fahr_to_celcius(temp)
        return conv_result

    def celcius_to_Fahr(self, C_temp):
        # Convert Celcius to Fahrenheit
        F_temp = (C_temp*(9/5)) + 32
        return F_temp
    
    def Fahr_to_celcius(self, F_temp):
        # Convert Fahrenheit to Celcius
        C_temp = (F_temp - 32)*(5/9)
        return C_temp 

    def zero_val_check(self, val):
        if val == 0:
            val = 1
        return val

    def tolerance_check_min(self, tolerance_min_val, tolerance_max_val, val):
        present_check = True
        # Checking 5% min of the val
        min_val_V1 = tolerance_min_val
        min_val_V2 = tolerance_min_val + (0.05 * self.zero_val_check(tolerance_max_val))
        if val >= min_val_V1 and val<= min_val_V2:
            print("MIN : {}, MAX : {:.2f}, CURRENT_VAL : {}".format(min_val_V1, min_val_V2, val))
            present_check = False
        return present_check

    def tolerance_check_max(self, tolerance_max_val, val):
        present_check = True
        # Checking 5% max of the val
        max_val_V1 = tolerance_max_val
        max_val_V2 = tolerance_max_val - (0.05 * self.zero_val_check(tolerance_max_val))
        if val >= max_val_V1 and val<= max_val_V2:
            print("MIN : {}, MAX : {}, CURRENT_VAL : {}".format(max_val_V1, max_val_V2, val))
            present_check = False
        return present_check
