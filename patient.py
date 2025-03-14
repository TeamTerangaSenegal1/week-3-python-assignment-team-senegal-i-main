# Patient Record Management
# Filename: patient.py
# Create a `Patient` class with:
# - `name` (string)
# - `age` (integer)
# - `medical_history` (list)
# Implement methods:
# - `add_medical_record(record)` → Adds a new record to `medical_history`.
# - `get_patient_details()` → Returns the patient's name, age, and medical history.

class Patient:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self.name = name
        self.age = age
        self.medical_history = []
    
    def add_medical_record(self, record):
        if record:
            self.medical_history.append(record)
        else:
            raise ValueError("Medical record cannot be empty.")
    
    def get_patient_details(self):
        return f"Name: {self.name} | Age: {self.age} | Medical History: {self.medical_history}"