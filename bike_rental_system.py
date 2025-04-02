import csv
from datetime import datetime
import os

# Starting with 100 bikes (default, overridden by CSV if it exists)
INITIAL_TOTAL_BIKES = 100
total_bikes = INITIAL_TOTAL_BIKES
rented_bikes = {}  # Dictionary to track rented bikes by user: {name: {'bikes': total, 'rentals': [{bikes: num, time: datetime}]}}

def load_state_from_csv():
    global total_bikes, rented_bikes
    filename = 'bike_rental_data.csv'
    if not os.path.isfile(filename):
        return  # If no CSV exists, keep default values (100 bikes)
    
    rented_bikes.clear()
    temp_rented_bikes = {}  # Temporary dict to build state
    
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["Name"]
            bikes_assigned = int(row["Bikes assign"])
            ongoing = int(row["Ongoing"])
            assign_time_str = row["Assign time"]
            drop_time_str = row["Drop time"]
            
            if assign_time_str != "-":  # Rent entry
                rent_time = datetime.strptime(assign_time_str, '%Y-%m-%d %H:%M:%S')
                if name not in temp_rented_bikes:
                    temp_rented_bikes[name] = {'bikes': 0, 'rentals': []}
                temp_rented_bikes[name]['rentals'].append({'bikes': bikes_assigned, 'time': rent_time})
                temp_rented_bikes[name]['bikes'] = ongoing  # Update with latest ongoing value
            
            if drop_time_str != "-":  # Drop entry
                # Drops are already reflected in 'Ongoing' of the rent entry, so no additional adjustment here
                pass
    
    # Copy to rented_bikes and calculate total_bikes
    rented_bikes.update(temp_rented_bikes)
    total_bikes_assigned = sum(data['bikes'] for data in rented_bikes.values())
    total_bikes = INITIAL_TOTAL_BIKES - total_bikes_assigned

def save_to_csv(data, is_header=False):
    file_exists = os.path.isfile('bike_rental_data.csv')
    with open('bike_rental_data.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists and not is_header:
            writer.writerow(["Name", "Bikes assign", "Ongoing", "Assign time", "Drop time", "Bill"])
        writer.writerow(data)

def rent_bike():
    global total_bikes
    print(f"Available bikes are: {total_bikes}")
    try:
        bikes_to_rent = int(input("How many bikes you want to rent?\n"))
    except ValueError:
        print("Please enter a valid number")
        return
    
    if total_bikes == 0 and bikes_to_rent == 0:
        print("You cannot rent 0 bikes! Please enter a number greater than 0")
        return
    if total_bikes == 0 and 0 <= bikes_to_rent <= 100:
        print("Currently there is no bikes available!")
        return  
    
    if bikes_to_rent > total_bikes:
        print("Sorry, not enough bikes available!")
        return
    
    if bikes_to_rent == 0:
        print("You cannot rent 0 bikes! Please enter a number greater than 0.")
        return
    
    name = input("Provide me your name: ")
    rent_time = datetime.now()
    
    total_bikes -= bikes_to_rent
    
    if name in rented_bikes:
        rented_bikes[name]['bikes'] += bikes_to_rent
        rented_bikes[name]['rentals'].append({'bikes': bikes_to_rent, 'time': rent_time})
    else:
        rented_bikes[name] = {
            'bikes': bikes_to_rent,
            'rentals': [{'bikes': bikes_to_rent, 'time': rent_time}]
        }
    
    total_user_bikes = rented_bikes[name]['bikes']
    save_to_csv([name, bikes_to_rent, total_user_bikes, rent_time.strftime('%Y-%m-%d %H:%M:%S'), "-", "-"])
    print(f"{bikes_to_rent} bikes assigned to you, {name}! Total bikes with you: {total_user_bikes}")

def drop_bike():
    global total_bikes
    print(f"Available bikes are: {total_bikes}")
    try:
        bikes_to_drop = int(input("How many bikes you want to drop? "))
    except ValueError:
        print("Please enter a valid number")
        return
    
    name = input("Enter your name for confirmation:\n")
    
    if name not in rented_bikes or rented_bikes[name]['bikes'] < bikes_to_drop:
        print("Error: You haven't rented that many bikes!")
        return
    
    drop_time = datetime.now()
    remaining_to_drop = bikes_to_drop
    bill = 0
    assign_times = []
    
    for rental in rented_bikes[name]['rentals']:
        if remaining_to_drop <= 0:
            break
        bikes_in_rental = rental['bikes']
        rent_time = rental['time']
        
        bikes_to_drop_from_this = min(remaining_to_drop, bikes_in_rental)
        time_used = int((drop_time - rent_time).total_seconds())
        bill += bikes_to_drop_from_this * time_used * 2
        
        if bikes_to_drop_from_this > 0:
            assign_times.append(rent_time.strftime('%Y-%m-%d %H:%M:%S'))
        
        rental['bikes'] -= bikes_to_drop_from_this
        remaining_to_drop -= bikes_to_drop_from_this
        
        if rental['bikes'] == 0:
            rented_bikes[name]['rentals'].remove(rental)
    
    rented_bikes[name]['bikes'] -= bikes_to_drop
    total_bikes += bikes_to_drop  # Add dropped bikes back to available
    remaining_bikes = rented_bikes[name]['bikes'] if rented_bikes[name]['bikes'] > 0 else 0
    
    bill_with_symbol = f"₹{bill}"
    assign_time_str = "; ".join(assign_times) if assign_times else "-"
    
    save_to_csv([name, bikes_to_drop, remaining_bikes, assign_time_str, drop_time.strftime('%Y-%m-%d %H:%M:%S'), bill_with_symbol])
    
    if remaining_bikes == 0:
        del rented_bikes[name]
    
    print(f"{bikes_to_drop} bikes dropped successfully!")
    print(f"Your bill for {bikes_to_drop} bikes is: {bill_with_symbol}")
    print(f"Remaining bikes with you: {remaining_bikes}")

# Load previous state from CSV at startup
load_state_from_csv()

# Main program with Ctrl+C handling
print("Welcome to Bike Rental Centre!")
try:
    while True:
        print("\n1. Rent Bike")
        print("2. Drop Bike")
        choice = input("Select option (1-2): ")
        
        if choice == "1":
            rent_bike()
        elif choice == "2":
            drop_bike()
        else:
            print("Invalid option! Please choose 1 or 2.")
except KeyboardInterrupt:
    print("\nThank you for using Bike Rental Centre! Goodbye!")
