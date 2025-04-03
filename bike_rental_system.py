import csv
from datetime import datetime
import os

INITIAL_TOTAL_BIKES = 100
total_bikes = INITIAL_TOTAL_BIKES
users = {}  # Dictionary: key = name, value = list of [bikes, rent_time] pairs

def load_state_from_csv():
    global total_bikes, users
    filename = 'bike_rental_data.csv'
    if not os.path.isfile(filename):
        return
    users.clear()
    temp_users = {}  # Temporary dict to track rentals per user
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)  # Read all rows to process sequentially
        # Step 1: Process rent entries
        for row in rows:
            name = row["Name"]
            assign = int(row["Bikes_assign"])
            assign_time = row["Assign_time"]
            drop_time = row["Drop_time"]
            if assign_time != "-" and drop_time == "-":  # Rent entry
                rent_time = datetime.strptime(assign_time, '%Y-%m-%d %H:%M:%S')
                if name not in temp_users:
                    temp_users[name] = []
                temp_users[name].append([assign, rent_time])  # Use assign as initial bikes
        # Step 2: Process drop entries
        for row in rows:
            name = row["Name"]
            drop = row["Drop"]
            drop_time = row["Drop_time"]
            if drop_time != "-" and drop != "-":  # Drop entry
                bikes_to_drop = int(drop)
                remaining_to_drop = bikes_to_drop
                if name in temp_users:
                    for rental in temp_users[name]:
                        if remaining_to_drop <= 0:
                            break
                        bikes_in_rental = rental[0]
                        bikes_to_drop_from_this = min(remaining_to_drop, bikes_in_rental)
                        rental[0] -= bikes_to_drop_from_this
                        remaining_to_drop -= bikes_to_drop_from_this
                    temp_users[name] = [rental for rental in temp_users[name] if rental[0] > 0]
                    if not temp_users[name]:
                        del temp_users[name]
    # Transfer to users
    for name, rentals in temp_users.items():
        users[name] = rentals
    total_bikes = INITIAL_TOTAL_BIKES - sum(sum(rental[0] for rental in user_rentals) for user_rentals in users.values())

def save_to_csv(data):
    file_exists = os.path.isfile('bike_rental_data.csv')
    with open('bike_rental_data.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Bikes_assign", "Drop", "Ongoing", "Assign_time", "Drop_time", "Bill"])
        writer.writerow(data)
#rent bikes
def rent_bike():
    global total_bikes
    print(f"Available bikes are: {total_bikes}")
    if total_bikes == 0:
        return
    try:
        bikes_to_rent = int(input("How many bikes you want to rent?\n"))
    except ValueError:
        print("Please enter a valid number")
        return
    if bikes_to_rent <= 0:
        print("You cannot rent 0 bikes! Please enter a number greater than 0.")
        return
    if bikes_to_rent > total_bikes:
        print("Sorry, not enough bikes available!")
        return
    name = input("Provide me your name: ")
    rent_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    rent_time_obj = datetime.strptime(rent_time, '%Y-%m-%d %H:%M:%S')
    if name not in users:
        users[name] = []
    users[name].append([bikes_to_rent, rent_time_obj])
    total_bikes -= bikes_to_rent
    total_user_bikes = sum(rental[0] for rental in users[name])
    save_to_csv([name, bikes_to_rent, "-", total_user_bikes, rent_time, "-", "-"])
    print(f"{bikes_to_rent} bikes assigned to you, {name}! Total bikes with you: {total_user_bikes}")

#drop bikes
def drop_bike():
    global total_bikes
    try:
        bikes_to_drop = int(input("How many bikes you want to drop?\n"))
    except ValueError:
        print("Please enter a valid number")
        return
    
    if bikes_to_drop <= 0:
        print("You cannot drop 0 bikes! Please enter a number greater than 0.")
        return
    
    name = input("Enter your name for confirmation: ")
    if name not in users or sum(rental[0] for rental in users[name]) < bikes_to_drop:
        print("Error: You haven't rented that many bikes!")
        return
    drop_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    drop_time_obj = datetime.strptime(drop_time, '%Y-%m-%d %H:%M:%S')
    
    remaining_to_drop = bikes_to_drop
    bill = 0
    assign_times = []
    original_assigned = 0
    rentals_copy = [[rental[0], rental[1]] for rental in users[name]]
    
    for i, rental in enumerate(users[name]):
        if remaining_to_drop <= 0:
            break
        bikes_in_rental = rental[0]
        rent_time = rental[1]
        bikes_to_drop_from_this = min(remaining_to_drop, bikes_in_rental)
        time_used = int((drop_time_obj - rent_time).total_seconds())
        bill += bikes_to_drop_from_this * time_used * 2
        if bikes_to_drop_from_this > 0:
            assign_times.append(rent_time.strftime('%Y-%m-%d %H:%M:%S'))
            original_assigned += rentals_copy[i][0]
        rental[0] -= bikes_to_drop_from_this
        remaining_to_drop -= bikes_to_drop_from_this
    
    users[name] = [rental for rental in users[name] if rental[0] > 0]
    total_bikes += bikes_to_drop
    remaining_bikes = sum(rental[0] for rental in users[name]) if users[name] else 0
    
    assign = original_assigned if original_assigned > 0 else bikes_to_drop
    assign_time_str = "; ".join(assign_times) if assign_times else "-"
    save_to_csv([name, assign, bikes_to_drop, remaining_bikes, assign_time_str, drop_time, f"₹{bill}"])
    
    if remaining_bikes == 0:
        del users[name]
    
    print(f"{bikes_to_drop} bikes dropped successfully!")
    print(f"Your bill for {bikes_to_drop} bikes is: ₹{bill}")
    print(f"Remaining bikes with you: {remaining_bikes}")

load_state_from_csv()
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
