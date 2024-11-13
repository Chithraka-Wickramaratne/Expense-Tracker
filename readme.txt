Here’s a README with headers and symbols as you requested:

---

# 📊 Expense Tracker CLI

A command-line **Expense Tracker** application developed in Python. This application allows users to record, manage, and analyze their personal finances, providing a straightforward way to track income and expenses, view summaries, and save or load data from a file.

## ✨ Features

- 📥 **Record New Entry**: Log income or expenses by entering type, amount, category, year, month, and date.
- 📄 **View All Entries**: Display a list of all recorded income and expense entries.
- 🧮 **Calculate Totals**: View total income, total expenses, and net balance (income vs. expenses).
- 📅 **Monthly Summary**: Get a summary of income and expenses for a specific month.
- 💾 **Save Data**: Save all recorded entries to a file (e.g., `.txt` or `.csv`).
- 📂 **Load Data**: Load financial data from a previously saved file.
- 🚪 **Exit**: Close the application safely.

## ⚙️ Technologies Used

- **Programming Language**: Python

## 🚀 Getting Started

### 🔧 Prerequisites

- **Python 3.x**

### 📥 Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Chithraka-Wickramaratne/Expense-Tracker.git
   cdExpense-Tracker
   ```

2. **Run the Program**:
   ```bash
   python expense_tracker.py
   ```

## 📖 Usage Guide

Upon running the program, you’ll see a menu with options:

1. **Record a New Entry**  
   - Input transaction details:
     - **Type**: Income or Expense
     - **Amount**: Transaction amount
     - **Category**: E.g., groceries, salary, rent
     - **Date**: Enter year, month, and day of the transaction

2. **View All Entries**  
   - Shows all recorded entries in a list format.

3. **Calculate Totals**  
   - Displays:
     - Total Income
     - Total Expense
     - Net Balance (Total Income - Total Expenses)

4. **Monthly Summary**  
   - Enter the specific month and year to view income and expenses for that period.

5. **Save Data**  
   - Input a filename (e.g., `expenses.txt` or `expenses.csv`) to save your financial data.

6. **Load Data**  
   - Load financial data from a previously saved file.

7. **Exit**  
   - Safely exit the application.

## 💾 Saving and Loading Data

- **Save Financial Data**: Choose a filename to save current entries to a file.
- **Load Financial Data**: Load data from a file, allowing you to continue where you left off.

## 📜 Example Session

```plaintext
Welcome to Expense Tracker!
Please choose an option:
1. Record a New Entry
2. View All Recorded Entries
3. Calculate Totals
4. View Summary For a Specific Month
5. Save Financial Data
6. Load Financial Data
7. Exit

> 1
Enter type (Income/Expense): Income
Enter amount: 500
Enter category: Salary
Enter year: 2024
Enter month: 11
Enter date: 13
Entry recorded successfully!

> 3
Total Income: $500
Total Expense: $0
Net Balance: $500

> 7
Goodbye!
```

## 📜 License

This project is open-source and available under the MIT License.

--- 
