import csv
import os
# Step 1: Create a new file
def make_new_file():
    file_name = input("Enter your file name: (just the name, no .csv): ") + ".csv"
    
    # Check if file doesn't exist yet
    if not os.path.exists(file_name):
        # Open file and add headers
        file = open(file_name, "w")
        file.write("ID,Name,Age\n")  # Headers for our table
        file.close()
        print(f"File '{file_name}' created successfully!")
    else:
        print("That file name is already taken!")
    return file_name

# Step 2: Add new information
def add_info(file_name):
    file = open(file_name, "a")  # "a" means add to end of file
    
    # Ask for information
    id_number = input("Enter the ID: ")
    name = input("Enter the name: ")
    age = input("Enter the Age: ")
    
    # Put all info together with commas
    new_line = id_number + "," + name + "," + age + "\n"
    file.write(new_line)
    file.close()
    print("Data added!")

# Step 3: Show all information
def show_info(file_name):
    file = open(file_name, "r")  # "r" means read
    all_lines = file.readlines()  # Get all lines
    for line in all_lines:
        print(line.strip())  # Show each line without extra spaces
    file.close()

# Step 4: Update information
def update_info(file_name):
    id_to_update = input("Enter the ID you want to update: ")
    found = False
    new_data = []
    
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == id_to_update:
                row[1] = input("Enter new Name: ")
                row[2] = input("Enter new Age: ")
                found = True
            new_data.append(row)
    
    if found:
        with open(file_name, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_data)
        print("Record updated successfully!")
    else:
        print("ID not found!")

def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File '{file_name}' has been deleted.")
    else:
        print("File does not exist!")

# Main program
def start_program():
    my_file = make_new_file()
    
    while True:  # Keep running until we say stop
        print("\nWhat do you want to do?")
        print("1. Write data")
        print("2. Read data")
        print("3. Update data")
        print("4. Delete file")
        print("5. Stop")
        
        choice = input("Pick a number: ")
        
        if choice == "1":
            add_info(my_file)
        elif choice == "2":
            show_info(my_file)
        elif choice == "3":
            update_info(my_file)
        elif choice == "4":
            delete_file(my_file)
        elif choice == "5":
            print("Goodbye!")
            break  # Stop the program
        else:
            print("That's not a valid number! Try 1, 2, 3, or 4")

# Start everything
start_program()
