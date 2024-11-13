# Import libraries
import sys
import csv
import calendar
import os
import re

financial_entries = []

def record_new_entry():
    type = input("Enter Type(Income/Expense): ").lower()

    if type not in ['income', 'expense']:
        print("\nError: Invalid type. Please enter 'Income' or 'Expense'.\n")
        return 
    
    while True:
        amount_str = input("Enter the Amount (Rs): ")

        if re.match(r'^\d+(\.\d+)?$', amount_str):
            amount = float(amount_str)
            if amount <= 0:
                print("\nError: Amount must be a positive value.\n")
                continue
            break
        else:
            print("\nError: Invalid amount. Please enter digits or decimal point only.\n")
            
    category = input("Enter the Category of " + type + " : ")

    while True:
        year = input("Enter Year of " + type + " (YYYY) : ")

        if not (year.isdigit() and len(year) == 4): 
            print("\nError: Invalid year format. Please enter a four-digit year.\n")
            continue
        year = int(year)  
        break 

    month = input("Enter Month of " + type + " (MM) [01 to 12]: ")

    try:
        month = int(month)
        if not 1 <= month <= 12:
            raise ValueError("\nMonth must be between 01 and 12.\n")
    except ValueError as ve:
        print(f"Error: {ve}")
        return  

    try:
        day = input("Enter Date of " + type + f" (DD) [01 to {calendar.monthrange(int(year), month)[1]}] : ")
        day = int(day)
        if not 1 <= day <= calendar.monthrange(int(year), month)[1]:
            raise ValueError(f"\nDay must be between 01 and {calendar.monthrange(int(year), month)[1]}.\n")
    except ValueError as ve:
        print(f"Error: {ve}")
        return
    new_entry = {'type': type, 'amount': amount, 'category': category, 'year': year, 'month': month, 'date': day}
    financial_entries.append(new_entry)

    print("\n==============================================\n")
    print("Entry Recorded Successfully!")
    print("\n==============================================\n")

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def view_all_entries():
    if not financial_entries:
        print("No entries recorded.")
    else:
        print("--- All Recorded Entries ---\n")

        for entry in financial_entries:
            print(f"Type: {entry['type']} | Amount: Rs{entry['amount']} | Category: {entry['category']}| Year:{entry['year']}| Month:{entry['month']} | Date: {entry['date']}")
            print()

def calculate_totals():
    
    total_income = 0
    total_expenses = 0

    
    for entry in financial_entries:
        try:
            amount = float(entry['amount'])
        except ValueError:
            print(f"Error: Invalid amount format for entry - {entry}")
            continue

        if entry['type'] == 'income':
            total_income += amount
        
        elif entry['type'] == 'expense':
            total_expenses += amount

    net_income = total_income - total_expenses

    print("\n==============================================\n")
    print(f"Total Income: Rs{total_income}")
    print(f"Total Expenses: Rs{total_expenses}")
    print(f"Net Income: Rs{net_income}")
    print("\n==============================================\n")

def view_summary():
    try:

        month_input = input("Enter the month (MM) [01 to 12]: ")
        month = int(month_input)
        if not 1 <= month <= 12:
            raise ValueError("\nInvalid month. Please enter a value between 01 and 12.\n")

       
        year_input = input("Enter the year (YYYY): ")
        if not year_input.isdigit() or len(year_input) != 4:
            raise ValueError("\nInvalid year format. Please enter a four-digit year.\n")

        year = int(year_input)

        
        filtered_entries = [entry for entry in financial_entries if is_entry_in_month(entry, month, year)]

        if not filtered_entries:
            print(f"\nNo entries found for {month}/{year}.\n")
            return

        
        total_income = sum(float(entry['amount']) for entry in filtered_entries if entry['type'] == 'income')
        total_expenses = sum(float(entry['amount']) for entry in filtered_entries if entry['type'] == 'expense')
        net_income = total_income - total_expenses

        print("\n==============================================\n")
        print(f"\n--- Summary for {month}/{year} ---")
        print(f"Total Income: Rs{total_income}")
        print(f"Total Expenses: Rs{total_expenses}")
        print(f"Net Income: Rs{net_income}\n")
        print("\n==============================================\n")

    except ValueError as ve:
        print(f"\nError: {ve}\n")



def is_entry_in_month(entry, target_month, target_year):

   
    entry_month, entry_year = map(int, [entry['month'], entry['year']])

 
    return entry_month == target_month and entry_year == target_year


def save_data():
    try:
        
        filename = input("Enter the filename to save financial data (example.txt or example.csv): ")

        
        valid_extensions = ['.csv', '.txt']
        if not any(filename.lower().endswith(ext) for ext in valid_extensions):
            raise ValueError("\nError: Invalid file format. Please enter a CSV or TXT file with the respective extension.\n")

        
        try:
            with open(filename, "w") as file:
                for entry in financial_entries:
                    file.write(f"{entry['type']},{entry['amount']},{entry['category']},{entry['year']},{entry['month']},{entry['date']}\n")

            print("\n==============================================\n")
            print(f"\nFinancial data saved to {filename} successfully.\n")
            print("\n==============================================\n")
        except Exception as e:
            print(f"\nError saving financial data: {e}\n")

    except ValueError as ve:
        print(f"\nError: {ve}\n")


def load_data():
    
    try:
        
        filename = input("Enter the filename to load financial data from (example.txt or example.csv): ")

        
        valid_extensions = ['.csv', '.txt']
        if not any(filename.lower().endswith(ext) for ext in valid_extensions):
            raise ValueError("\nError: Invalid file format. Please enter a CSV or TXT file with the respective extension.\n")

       
        try:
            
            with open(filename, "r") as file:
                
                if filename.lower().endswith('.csv'):
                    reader = csv.reader(file)
                else:
                    reader = file.readlines()

               
                financial_entries.clear()

                
                if filename.lower().endswith('.csv'):
                    for row in reader:
                        entry = {
                            'type': row[0],
                            'amount': row[1],
                            'category': row[2],
                            'year': row[3],
                            'month': row[4],
                            'date': row[5]
                        }
                        financial_entries.append(entry)
                else:
                    for line in reader:
                        
                        values = line.strip().split(',')
                        entry = {
                            'type': values[0],
                            'amount': values[1],
                            'category': values[2],
                            'year': values[3],
                            'month': values[4],
                            'date': values[5]
                        }
                        financial_entries.append(entry)

            print("\n==============================================\n")
            print(f"Financial data loaded from {filename} successfully.")
            print("\n==============================================\n")

        except FileNotFoundError:
            print(f"\nError: File '{filename}' not found.\n")
        except Exception as e:
            print(f"\nError loading financial data: {e}\n")

    except ValueError as ve:
        print(f"\nError: {ve}\n")


try:
    while True:
        
        print("\n1). Record a New Entry")
        print("2). View All Recorded Entries")
        print("3). Calculate Totals")
        print("4). View Summary For a Specific Month")
        print("5). Save Financial Data")
        print("6). Load financial Data")
        print("7). Exit\n")

 
        choice = input("Enter Your Choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("\nPlease enter a valid number.")
            continue

        print()
        
        if choice in [1, 2, 3, 4, 5, 6, 7]:
            if choice == 1:
                record_new_entry()
            elif choice == 2:
                view_all_entries()
            elif choice == 3:
                calculate_totals()
            elif choice == 4:
                view_summary()
            elif choice == 5:
                save_data()
            elif choice == 6:
                load_data()
            elif choice == 7:
                break
        else:
            print("\nPlease Enter a Valid Number (1 to 7).\n")

except:
    print("\nAn error occurred. Exiting the program.\n")