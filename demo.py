import csv import time from datetime import datetime

CSV_FILE = "bike_rental_data.csv" RATE_PER_SECOND = 2  # Rs. 2 per second

def initialize_csv(): try: with open(CSV_FILE, "x", newline="") as file: writer = csv.writer(file) writer.writerow(["Name", "Bikes Rented", "Status", "Time", "Bill"]) except FileExistsError: pass

def rent_bike(): name = input("Enter your name: ") num_bikes = int(input("How many bikes do you want to rent? ")) rent_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(CSV_FILE, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, num_bikes, "Ongoing", rent_time, 0])

print(f"{name}, you have rented {num_bikes} bike(s) at {rent_time}. Billing will be calculated per second.")

def drop_bike(): name = input("Enter your name for confirmation: ") drop_bikes = int(input("How many bikes do you want to drop? "))

rows = []
found = False

with open(CSV_FILE, "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        if row[0] == name and row[2] == "Ongoing":
            found = True
            rented_bikes = int(row[1])
            rent_time = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
            seconds_rented = (datetime.now() - rent_time).seconds
            total_bill = rented_bikes * RATE_PER_SECOND * seconds_rented
            if drop_bikes >= rented_bikes:
                row[2] = "Completed"
            else:
                row[1] = str(rented_bikes - drop_bikes)
            row[4] = round(total_bill, 2)
        rows.append(row)

if not found:
    print("No active rental found under this name.")
    return

with open(CSV_FILE, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Bikes Rented", "Status", "Time", "Bill"])
    writer.writerows(rows)

print(f"{name}, you have returned {drop_bikes} bike(s). Your final bill is Rs. {round(total_bill, 2)}.")

def main(): initialize_csv() try: while True: print("\nWelcome to the Bike Rental Center") print("1. Rent a Bike") print("2. Drop a Bike") choice = input("Choose an option: ")

if choice == "1":
            rent_bike()
        elif choice == "2":
            drop_bike()
        else:
            print("Invalid option. Please try again.")
except KeyboardInterrupt:
    print("\nThank you for using our service! Goodbye!")

if name == "main": main()

