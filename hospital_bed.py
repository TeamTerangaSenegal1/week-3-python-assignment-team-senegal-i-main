# Hospital Bed Allocation System
# Filename: hospital_bed.py
# Create a `HospitalBed` class with:
# - `bed_number`
# - `patient_name` (default `None`)
# Implement methods:
# - `assign_bed(patient_name)` → Assigns a patient to the bed.
# - `release_bed()` → Frees up the bed

class HospitalBed:
    def __init__(self, bed_number, patient_name=None):
        self.bed_number = bed_number
        self.patient_name = patient_name

    def assign_bed(self, patient_name):
        if not self.patient_name:
            self.patient_name = patient_name
        else:
            raise ValueError("Bed is already assigned.")

    def release_bed(self):
        self.patient_name = None
