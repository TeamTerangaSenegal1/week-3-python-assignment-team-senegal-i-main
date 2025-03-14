# Vital Signs Monitoring System
# Filename: vital_signs.py
# Create a `VitalSigns` class with:
# - `patient_name`
# - `heart_rate`
# - `blood_pressure`
# Implement methods:
# - `update_vitals(hr, bp)` → Updates heart rate and blood pressure.
# - `is_critical()` → Returns `True` if heart rate < 50 or > 120, or blood pressure is too high/low.

class VitalSigns:
    def __init__(self, patient_name, heart_rate, blood_pressure):
        self.patient_name = patient_name
        self.heart_rate = heart_rate
        self.blood_pressure = blood_pressure

    def update_vitals(self, hr, bp):
        self.heart_rate = hr
        self.blood_pressure = bp
    
    def is_critical(self):
        if self.heart_rate < 50 or self.heart_rate > 120 or self.blood_pressure < 80 or self.blood_pressure > 120:
            return True

    