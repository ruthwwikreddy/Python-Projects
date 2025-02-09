import csv

class EcoPulse:
    def __init__(self):
        self.plant_data = self.load_plant_data_from_csv()
        self.nursery_data = self.load_nursery_data_from_csv()
        self.tips_data = self.load_tips_data_from_csv()

    def load_plant_data_from_csv(self):
        plant_data = {}
        with open('plant_data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                plant_name = row['Plant']
                npk_recommendation = {
                    'Nitrogen': row['N'], 'Phosphorus': row['P'], 'Potassium': row['K']
                }

                plant_data[plant_name] = {
                    'Scientific Name': row['Scientific Name'],
                    'Type': row['Type'],
                    'Watering': row['Watering'],
                    'Light Requirements': row['Light Requirements'],
                    'Soil Type': row['Soil Type'],
                    'Common Issues': row['Common Issues'],
                    'NPK Recommendation': npk_recommendation
                }

        return plant_data

    def load_nursery_data_from_csv(self):
        nursery_data = {}
        with open('plant_data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                city = row['City']
                nursery_data[city] = {
                    'Name': row['Name'],
                    'Address': row['Address'],
                    'Phone': row['Phone']
                }

        return nursery_data

    def load_tips_data_from_csv(self):
        tips_data = {}
        with open('plant_data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                plant_name = row['Plant']
                tips_data[plant_name] = row['Tip']

        return tips_data

    def display_plant_list(self):
        print("Plants in the pulse:")
        for plant_name in self.plant_data:
            print(f"- {plant_name}")

    def get_nursery_info(self, city):
        nursery_info = self.nursery_data.get(city)
        if nursery_info:
            print("\nNursery Information:")
            print(f"Name: {nursery_info['Name']}")
            print(f"Address: {nursery_info['Address']}")
            print(f"Phone: {nursery_info['Phone']}")
        else:
            print(f"No nursery information available for {city}.")

    def get_plant_details(self, plant_name):
        plant_details = self.plant_data.get(plant_name)
        if plant_details:
            print("\nPlant Details:")
            print(f"Name: {plant_name}")
            print(f"Scientific Name: {plant_details.get('Scientific Name', 'N/A')}")
            print(f"Type: {plant_details.get('Type', 'N/A')}")
            print(f"Watering: {plant_details.get('Watering', 'N/A')}")
            print(f"Light Requirements: {plant_details.get('Light Requirements', 'N/A')}")
            print(f"Soil Type: {plant_details.get('Soil Type', 'N/A')}")
            print(f"Common Issues: {plant_details.get('Common Issues', 'N/A')}")
            print("NPK Recommendation:")
            for nutrient, recommendation in plant_details.get('NPK Recommendation', {}).items():
                print(f"  {nutrient}: {recommendation}")
        else:
            print(f"Plant details not found for '{plant_name}'.")

    def get_gardening_tips(self):
        plant_name = input("Enter the name of the plant: ").strip()
        tip = self.tips_data.get(plant_name)
        if tip:
            print(f"Gardening Tip for {plant_name}: {tip}")
        else:
            print("No specific tips available for this plant.")

    def display_plant_pulse_menu(self):
        print("\n===== EcoPulse - Your Intelligent Plant Care Assistant! =====")
        print("1. Display plant list")
        print("2. Get nursery information")
        print("3. Get plant details")
        print("4. Gardening Tips from Experts")
        print("5. View Plant Care Calendar")
        print("0. Exit")

    def plant_pulse_menu(self):
        while True:
            self.display_plant_pulse_menu()
            choice = input("Please select a command (1/2/3/4/5/0): ").strip()

            if choice == "1":
                self.display_plant_list()
            elif choice == "2":
                city = input("Enter city to get nursery information: ").strip()
                self.get_nursery_info(city)
            elif choice == "3":
                plant_name = input("Enter the name of the plant: ").strip()
                self.get_plant_details(plant_name)
            elif choice == "4":
                self.get_gardening_tips()
            elif choice == "5":
                print("View Plant Care Calendar functionality coming soon...")
            elif choice == "0":
                print("Exiting EcoPulse.")
                break
            else:
                print("Invalid command. Please select a valid option.")

if __name__ == "__main__":
    plant_pulse = EcoPulse()
    plant_pulse.plant_pulse_menu()
