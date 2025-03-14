# COVID-19 Test Center Management
# Filename: covid_test.py
# Create a `CovidTest` class with:
# - `patient_name`
# - `test_date`
# - `result` (default `Pending`)
# Implement methods:
# - `update_result(new_result)` → Updates test result (Positive/Negative).
# - `get_test_info()` → Returns patient name, test date, and result.

class CovidTest:
    def __init__(self, patient_name, test_date):
        self.patient_name = patient_name
        self.test_date = test_date
        self.result = "Pending"
    
    def update_result(self, new_result):
        if new_result in ["Positive", "Negative"]:
            self.result = new_result
        else:
            raise ValueError("Result must be either 'Positive' or 'Negative'.")

    def get_test_info(self):
        return f"Patient: {self.patient_name} | Test Date: {self.test_date} | Result: {self.result}"