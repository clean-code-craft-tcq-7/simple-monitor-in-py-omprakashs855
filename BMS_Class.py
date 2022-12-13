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
                # Discharging
                "Discharge_Temp_Min" : -20,
                "Discharge_Temp_Max" : 65,
                "SOC_min" : 20,
                "SOC_max" : 80,
                "Charge_rate": 0.8
            }
        ]
        return battery_bms_info
    
    def celcius_to_Fahr(self, C_temp):
        # Convert Celcius to Fahrenheit
        F_temp = (C_temp*(9/5)) + 32
        return F_temp
    
    def Fahr_to_celcius(self, F_temp):
        # Convert Fahrenheit to Celcius
        C_temp = (F_temp - 32)*(5/9)
        return C_temp 