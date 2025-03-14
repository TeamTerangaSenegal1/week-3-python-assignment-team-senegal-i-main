# Doctor Information System
# Filename: doctor.py
# Create a `Doctor` class with:
# - `name`
# - `specialization`
# - `patients` (list)
# Implement methods:
# - `add_patient(patient_name)` → Adds a patient's name to the list.
# - `list_patients()` → Returns all assigned patients.

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.patients = []
    
    def add_patient(self, patient_name):
        if patient_name:
            self.patients.append(patient_name)
        else:
            raise ValueError("Patient name cannot be empty.")

    def list_patients(self):
        return self.patients