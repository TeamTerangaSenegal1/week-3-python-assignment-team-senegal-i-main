# Medical Imaging Analysis System
# Filename: mri_scan.py
# Create an `MRI_Scan` class with:
# - `patient_name`
# - `scan_date`
# - `findings` (default `None`)
# Implement methods:
# - `add_findings(report)` → Updates the scan findings.
# - `get_scan_details()` → Returns patient name, date, and findings.

class MRI_Scan:
    def __init__(self, patient_name, scan_date):
        self.patient_name = patient_name
        self.scan_date = scan_date
        self.findings = None
    
    def add_findings(self, report):
        if report:
            self.findings = report
        else:
            raise ValueError("Findings cannot be empty.")

    def get_scan_details(self):
        return f"Patient: {self.patient_name} | Scan Date: {self.scan_date} | Findings: {self.findings}"