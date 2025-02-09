import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import Tk, Label, Entry, Button, messagebox, Checkbutton, IntVar
import os
from fpdf import FPDF

# Define the structure of the apartment building
floors = 3
flats_per_floor = 3

# File to save data
data_file = 'apartment_rent_data.csv'

def input_rent_data():
    data = []
    for floor in range(1, floors + 1):
        for flat in range(1, flats_per_floor + 1):
            rent = input(f"Enter the rent for Floor {floor}, Flat {flat}: ")
            try:
                rent = float(rent)
                paid = input(f"Is the rent for Floor {floor}, Flat {flat} paid (yes/no)? ").strip().lower()
                paid = paid == 'yes'
                data.append({
                    'Floor': floor,
                    'Flat': flat,
                    'Rent': rent,
                    'Paid': paid
                })
            except ValueError:
                print(f"Invalid rent value entered for Floor {floor}, Flat {flat}. Please enter a numeric value.")
                return pd.DataFrame()  # Return empty DataFrame to handle errors
    return pd.DataFrame(data)

def load_data():
    if os.path.exists(data_file):
        try:
            df = pd.read_csv(data_file)
            if df.empty:
                print("Data file is empty. Entering new data.")
                df = input_rent_data()
                save_data(df)
            return df
        except pd.errors.EmptyDataError:
            print("Data file is empty. Entering new data.")
            df = input_rent_data()
            save_data(df)
            return df
    else:
        print("Data file not found. Entering new data.")
        df = input_rent_data()
        save_data(df)
        return df

def save_data(df):
    df.to_csv(data_file, index=False)

def validate_rent(value):
    try:
        value = float(value)
        if value < 0:
            raise ValueError("Rent cannot be negative.")
        return value
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Invalid rent value: {e}")
        return None

def analyze_data(df):
    average_rent = df['Rent'].mean()
    median_rent = df['Rent'].median()
    max_rent = df['Rent'].max()
    min_rent = df['Rent'].min()

    floor_stats = df.groupby('Floor')['Rent'].agg(['mean', 'median', 'max', 'min'])

    return average_rent, median_rent, max_rent, min_rent, floor_stats

def plot_data(df, floor_stats):
    if df.empty:
        print("No data available for plotting.")
        return

    plt.figure(figsize=(10, 6))

    # Bar plot for average rent by floor
    plt.bar(floor_stats.index, floor_stats['mean'], color='skyblue')
    plt.title('Average Rent by Floor')
    plt.xlabel('Floor')
    plt.ylabel('Average Rent')
    plt.xticks(floor_stats.index)
    
    plt.tight_layout()
    plt.show()

def generate_report(df, floor_stats):
    # Generate PDF Report
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Apartment Rental Analysis Report", ln=True, align='C')
    pdf.ln(10)
    
    pdf.cell(200, 10, txt=f"Average Rent: ${df['Rent'].mean():.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Median Rent: ${df['Rent'].median():.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Maximum Rent: ${df['Rent'].max():.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Minimum Rent: ${df['Rent'].min():.2f}", ln=True)
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Floor-wise Rental Statistics:", ln=True)
    for floor, stats in floor_stats.iterrows():
        pdf.cell(200, 10, txt=f"Floor {floor} - Mean: ${stats['mean']:.2f}, Median: ${stats['median']:.2f}, Max: ${stats['max']:.2f}, Min: ${stats['min']:.2f}", ln=True)
    
    pdf.output("rental_analysis_report.pdf")
    
    # Generate Excel Report
    with pd.ExcelWriter('rental_analysis_report.xlsx') as writer:
        df.to_excel(writer, sheet_name='Rent Data', index=False)
        floor_stats.to_excel(writer, sheet_name='Floor Stats')

def main_gui():
    def submit_data():
        try:
            rent = validate_rent(rent_entry.get())
            if rent is not None:
                floor = int(floor_entry.get())
                flat = int(flat_entry.get())
                paid = paid_var.get() == 1
                df = pd.DataFrame([{'Floor': floor, 'Flat': flat, 'Rent': rent, 'Paid': paid}])
                if os.path.exists(data_file):
                    existing_df = pd.read_csv(data_file)
                    df = pd.concat([existing_df, df])
                save_data(df)
                messagebox.showinfo("Success", "Rent data saved successfully.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid floor and flat numbers.")
    
    root = Tk()
    root.title("Apartment Rent Input")

    Label(root, text="Floor Number:").grid(row=0, column=0)
    floor_entry = Entry(root)
    floor_entry.grid(row=0, column=1)

    Label(root, text="Flat Number:").grid(row=1, column=0)
    flat_entry = Entry(root)
    flat_entry.grid(row=1, column=1)

    Label(root, text="Rent:").grid(row=2, column=0)
    rent_entry = Entry(root)
    rent_entry.grid(row=2, column=1)

    paid_var = IntVar()
    paid_check = Checkbutton(root, text="Rent Paid", variable=paid_var)
    paid_check.grid(row=3, columnspan=2)

    Button(root, text="Submit", command=submit_data).grid(row=4, columnspan=2)

    root.mainloop()

def main():
    df = load_data()
    
    average_rent, median_rent, max_rent, min_rent, floor_stats = analyze_data(df)

    print("\nApartment Rental Data:")
    print(df)

    print("\nRental Statistics:")
    print(f"Average Rent: ${average_rent:.2f}")
    print(f"Median Rent: ${median_rent:.2f}")
    print(f"Maximum Rent: ${max_rent:.2f}")
    print(f"Minimum Rent: ${min_rent:.2f}")

    print("\nFloor-wise Rental Statistics:")
    print(floor_stats)

    try:
        plot_data(df, floor_stats)
    except ImportError:
        print("\nMatplotlib or Seaborn not installed. Install them for graphical visualization.")

    generate_report(df, floor_stats)

if __name__ == "__main__":
    # Uncomment the line below to use the GUI for data entry
    # main_gui()
    # Uncomment the line below to use the CLI for data entry and analysis
    main()
