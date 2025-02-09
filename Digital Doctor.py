import logging

class TelemedicineRobot:
    def __init__(self):
        self.patient_info = {}
        self.medical_history = {}
        self.medicines = {
            "Children (0-12)": [
                {"Medicine Name": "Dabur Honitus Syrup", "Purpose": "Cough", "Dosage": "As directed by a pediatrician"},
                {"Medicine Name": "Sinarest-PD Syrup", "Purpose": "Cold and Fever", "Dosage": "As directed by a pediatrician"},
                {"Medicine Name": "Crocin Drops", "Purpose": "Fever and Pain", "Dosage": "As directed by a pediatrician"},
                {"Medicine Name": "Calpol 120mg Suspension", "Purpose": "Fever and Pain", "Dosage": "As directed by a pediatrician"},
                {"Medicine Name": "P-250 Suspension", "Purpose": "Fever and Pain", "Dosage": "As directed by a pediatrician"},
                {"Medicine Name": "Nasivion Pediatric Drops", "Purpose": "Nasal congestion", "Dosage": "As directed by a pediatrician"},
                {"Medicine Name": "Colicaid Drops", "Purpose": "Infant colic", "Dosage": "As directed by a pediatrician"},
            ],
            "Adults (13+)": [
                {"Medicine Name": "Vicks Cough Drops", "Purpose": "Cough", "Dosage": "As directed on the package"},
                {"Medicine Name": "Vicks Action 500", "Purpose": "Cold and Fever", "Dosage": "1 tablet every 4-6 hours as needed"},
                {"Medicine Name": "Crocin", "Purpose": "Fever and Pain", "Dosage": "1-2 tablets every 4-6 hours as needed"},
                {"Medicine Name": "Paracetamol 500mg", "Purpose": "Fever and Pain", "Dosage": "1-2 tablets every 4-6 hours as needed"},
                {"Medicine Name": "Dolo 650", "Purpose": "Fever and Pain", "Dosage": "1-2 tablets every 4-6 hours as needed"},
                {"Medicine Name": "Aspirin", "Purpose": "Fever and Pain", "Dosage": "As directed by a healthcare provider"},
                {"Medicine Name": "Vicks Inhaler", "Purpose": "Nasal congestion", "Dosage": "As directed on the package"},
                {"Medicine Name": "Sudafed", "Purpose": "Nasal congestion", "Dosage": "As directed on the package"},
            ],
            "All Ages": [
                {"Medicine Name": "Benadryl", "Purpose": "Allergies", "Dosage": "As directed on the package"},
                {"Medicine Name": "Otrivin Nasal Spray", "Purpose": "Nasal congestion", "Dosage": "As directed on the package"},
                {"Medicine Name": "Strepsils", "Purpose": "Sore throat", "Dosage": "As directed on the package"},
                {"Medicine Name": "Halls", "Purpose": "Sore throat", "Dosage": "As directed on the package"},
                {"Medicine Name": "Digene", "Purpose": "Indigestion", "Dosage": "As directed on the package"},
                {"Medicine Name": "Eno", "Purpose": "Indigestion", "Dosage": "As directed on the package"},
                {"Medicine Name": "Zyrtec", "Purpose": "Allergies", "Dosage": "As directed on the package"},
                {"Medicine Name": "Allegra", "Purpose": "Allergies", "Dosage": "As directed on the package"},
                {"Medicine Name": "Saridon", "Purpose": "Headache", "Dosage": "As directed on the package"},
                {"Medicine Name": "Combiflam", "Purpose": "Headache and Pain", "Dosage": "As directed on the package"},
            ]
        }

    def start_consultation(self):
        print("Welcome to the Telemedicine Robot!")
        print("Please provide some information before we begin.")
        self.collect_patient_info()
        self.collect_medical_history()
        self.perform_consultation()

    def collect_patient_info(self):
        print("\nPatient Information:")
        self.patient_info["name"] = input("Name: ")
        self.patient_info["age"] = input("Age: ")
        self.patient_info["gender"] = input("Gender: ")

    def collect_medical_history(self):
        print("\nMedical History:")
        self.medical_history["medical_condition"] = input("Medical condition: ")
        self.medical_history["medications"] = input("Current medications (if any): ")
        self.medical_history["allergies"] = input("Allergies (if any): ")

    def perform_consultation(self):
        print("\nLet's start the consultation.")
        print(f"Patient Name: {self.patient_info['name']}")
        print(f"Age: {self.patient_info['age']}")
        print(f"Gender: {self.patient_info['gender']}")
        print("\nMedical History:")
        print(f"Medical Condition: {self.medical_history['medical_condition']}")
        print(f"Current Medications: {self.medical_history['medications']}")
        print(f"Allergies: {self.medical_history['allergies']}")

        # Ask the patient about their purpose
        patient_purpose = input("\nWhat is your current health issue (e.g., cough, cold, fever, headache)? ").strip().lower()

        # Display medicines based on age group and purpose
        age_group = self.get_age_group()
        if age_group in self.medicines:
            print(f"\nMedicines for {age_group} for {patient_purpose}:")
            for medicine_info in self.medicines[age_group]:
                if patient_purpose in medicine_info["Purpose"].lower():
                    print(f"{medicine_info['Medicine Name']} - Dosage: {medicine_info['Dosage']}")
        else:
            print(f"No specific medicines listed for age group: {age_group}")

            # Simulate a medical consultation
        print("\nDoctor: How can I assist you today?")
        patient_question = input("Patient: ")

        # Log the interaction
        self.log_interaction(patient_question)

        print("Doctor: I recommend consulting with a healthcare professional for further evaluation.")

    def log_interaction(self, patient_question):
        # Basic logging example
        logging.basicConfig(filename='consultation_logs.log', level=logging.INFO)
        logging.info(f"Patient: {self.patient_info['name']} - Question: {patient_question}")

        provide_doctor_contacts = input("Would you like contact information for specific types of doctors? (yes/no): ").strip().lower()
        if provide_doctor_contacts == 'yes':
            self.provide_doctor_contacts()

    def provide_doctor_contacts(self):
        print("\nTypes of Doctors:")
        print("1. General Physician")
        print("2. Pediatrician")
        print("3. Cardiologist")
        print("4. Dermatologist")
        print("5. Gynecologist/Obstetrician")
        print("6. Orthopedic Surgeon")
        print("7. Psychiatrist")
        print("8. Ophthalmologist")
        print("9. Gastroenterologist")
        print("10. ENT Specialist")

        selected_types = input("\nEnter the numbers of the types of doctors you are interested in (comma-separated): ").strip()
        selected_types = [int(x) for x in selected_types.split(',')]

        for doctor_type in selected_types:
            self.display_doctor_contact(doctor_type)

    def display_doctor_contact(self, doctor_type):
        contacts = {
            1: {"Type": "General Physician", "Contact": "Dr. Smith - Phone: XXX-XXXX"},
            2: {"Type": "Pediatrician", "Contact": "Dr. Johnson - Phone: XXX-XXXX"},
            3: {"Type": "Cardiologist", "Contact": "Dr. Davis - Phone: XXX-XXXX"},
            4: {"Type": "Dermatologist", "Contact": "Dr. Wilson - Phone: XXX-XXXX"},
            5: {"Type": "Gynecologist/Obstetrician", "Contact": "Dr. Miller - Phone: XXX-XXXX"},
            6: {"Type": "Orthopedic Surgeon", "Contact": "Dr. Brown - Phone: XXX-XXXX"},
            7: {"Type": "Psychiatrist", "Contact": "Dr. Taylor - Phone: XXX-XXXX"},
            8: {"Type": "Ophthalmologist", "Contact": "Dr. Anderson - Phone: XXX-XXXX"},
            9: {"Type": "Gastroenterologist", "Contact": "Dr. Moore - Phone: XXX-XXXX"},
            10: {"Type": "ENT Specialist", "Contact": "Dr. White - Phone: XXX-XXXX"},
        }

        if doctor_type in contacts:
            doctor_info = contacts[doctor_type]
            print(f"\nContact Information for {doctor_info['Type']}:")
            print(doctor_info['Contact'])
        else:
            print(f"\nNo contact information available for the selected doctor type.")

if __name__ == "__main__":
    telemedicine_robot = TelemedicineRobot()
    telemedicine_robot.start_consultation()