# Pharmacy Prescription System
# Filename: prescription.py
# Create a `Prescription` class with:
# - `patient_name`
# - `medications` (dictionary with drug names as keys and dosages as values)
# Implement methods:
# - `add_medication(drug, dosage)` → Adds a drug and dosage.
# - `view_prescription()` → Displays all prescribed medications.

class Prescription:
    def __init__(self, patient_name):
        self.patient_name = patient_name
        self.medications = {}
    
    def add_medication(self, drug, dosage):
        if drug and dosage:
            self.medications[drug] = dosage
        else:
            raise ValueError("Both drug and dosage must be provided.")

    def view_prescription(self):
        return self.medications