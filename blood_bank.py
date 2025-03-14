# Blood Bank Management System
# Filename: blood_bank.py
# Create a `BloodBank` class with:
# - `blood_type`
# - `units_available`
# Implement methods:
# - `donate_blood(units)` → Increases the units available.
# - `request_blood(units)` → Decreases units if enough stock exists.

class BloodBank:
    def __init__(self, blood_type, units_available=0):
        self.blood_type = blood_type
        self.units_available = max(0, units_available)

    def donate_blood(self, units):
        if units > 0:
            self.units_available += units
        else:
            raise ValueError("Units must be a positive number.")

    def request_blood(self, units):
        if units > 0 and self.units_available >= units:
            self.units_available -= units
        else:
            raise ValueError("Not enough blood units available or invalid request.")