import time
import csv
from datetime import datetime

class BikeRentalSystem:
    def __init__(self, total_bikes=100):
        self.total_bikes = total_bikes
        self.available_bikes = total_bikes
        self.rented_bikes = {}  # {name: [(num_bikes, rent_time), ...]}
        self.filename = "bike_rental_records.csv"
        self.initialize_csv()

    def initialize_csv(self):
        try:
            with open(self.filename, 'x', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Bikes", "Rent Time", "Drop Time", "Transaction Time", "Bill"])
        except FileExistsError:
            pass

    def rent_bike(self):
        if self.available_bikes == 0:
            print("Sorry, no bikes available for rent.")
            return
        
        try:
            num_bikes = int(input("How many bikes do you want to rent? "))
            if num_bikes > self.available_bikes or num_bikes <= 0:
                print("Invalid number of bikes requested.")
                return
        except ValueError:
            print("Please enter a valid number.")
            return
        
        name = input("Provide me your name: ")
        self.available_bikes -= num_bikes
        rent_time = time.time()
        
        if name in self.rented_bikes:
            self.rented_bikes[name].append((num_bikes, rent_time))
        else:
            self.rented_bikes[name] = [(num_bikes, rent_time)]
        
        print(f"Bike assigned to you, {name}.")
        print(f"Remaining bikes: {self.available_bikes}")
        print("Press Ctrl+C to exit.")
        
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S")
        self.write_to_csv(name, num_bikes, rent_time, "Ongoing", time_str, "-")
        
    def drop_bike(self):
        name = input("Enter your name for confirmation: ")
        if name not in self.rented_bikes:
            print("No record found for this name.")
            return
        
        total_rented_bikes = sum(bikes for bikes, _ in self.rented_bikes[name])
        try:
            drop_bikes = int(input(f"You have {total_rented_bikes} bikes. How many do you want to drop? "))
            if drop_bikes > total_rented_bikes or drop_bikes <= 0:
                print("Invalid number of bikes to drop.")
                return
        except ValueError:
            print("Please enter a valid number.")
            return
        
        drop_time = time.time()
        bill = 0
        remaining_bikes = []
        
        for num_bikes, rent_time in self.rented_bikes[name]:
            if drop_bikes == 0:
                remaining_bikes.append((num_bikes, rent_time))
                continue
            
            if drop_bikes >= num_bikes:
                duration = int(drop_time - rent_time)
                bill += num_bikes * duration * 2
                drop_bikes -= num_bikes
            else:
                duration = int(drop_time - rent_time)
                bill += drop_bikes * duration * 2
                remaining_bikes.append((num_bikes - drop_bikes, rent_time))
                drop_bikes = 0
        
        self.available_bikes += (total_rented_bikes - len(remaining_bikes))
        
        if remaining_bikes:
            self.rented_bikes[name] = remaining_bikes
        else:
            del self.rented_bikes[name]
        
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S")
        
        print(f"Name matched. Total bill for dropped bikes: ₹{bill}")
        print(f"Remaining bikes: {self.available_bikes}")
        self.write_to_csv(name, total_rented_bikes - len(remaining_bikes), drop_time, time.ctime(drop_time), time_str, bill)
    
    def write_to_csv(self, name, num_bikes, rent_time, drop_time, time_str, bill):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, num_bikes, time.ctime(rent_time), drop_time, time_str, bill])

if __name__ == "__main__":
    bike_rental_system = BikeRentalSystem()
    while True:
        print("\nWelcome to Bike Rental Centre")
        print("1. Rent Bike")
        print("2. Drop Bike")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            bike_rental_system.rent_bike()
        elif choice == '2':
            bike_rental_system.drop_bike()
        elif choice == '3':
            print("Thank you for using the Bike Rental Centre!")
            break
        else:
            print("Invalid choice, please try again.")
