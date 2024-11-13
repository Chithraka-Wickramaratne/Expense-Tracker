==========  Project: Text-Based Finance Tracker  ==========

## Overview
-----------------

The purpose of this financial management system is to assist users in keeping track of their earnings and outlays, examining summaries, and effectively managing financial information. The system's console-based menu offers an intuitive user interface.

## Usage
-----------------

1). **Record a New Entry**: If User Choose Option 1, Can enter inputs (type,ammount,category,year,month,date)

2). **View All Recorded Entries**: If User Option Choose 2, User can see all the records that he enterd

3). **Calculate Totals**: If User choos Option 3,Calculate and display the total income, total expenses, and net income.

4). **View Summary For a Specific Month**: If User choos Option 4, View a summary of a specific month and year.
	Ex: User wants to View year 2024th first month summary, User can input Year as 2024 and month 01 

5). **Save Financial Data**: IF User choose 5, Save financial data to a csv or txt file. The user can choose between txt and csv file formats.User Can save a file only if given file exsist the device.(Sometimes if user inputs only file name, entries are not recorded to the file. If this occures give fully file path, then it will resolve)
	Ex: User enters example.csv as a file name, data will be save to csv file

6). **Load Financial Data**: If User choose 6, Load financial data from a csv or txt file

7). **Exit**: If User choose 7, Exit the program.

## Challenges Faced
-----------------

- Ensuring proper validation for user inputs, such as numeric values and correct date formats.
- Managing different file formats (csv and txt) for saving and loading financial data.
- Being unfamilliar with some Libraries was a big challenge
- Some functions were not interact propperly with other functions

## Solutions Implemented
-----------------

- Put input validation into place to make sure users enter data accurately for amount, type, date, etc.
- Added support for both .csv and .txt file formats, allowing users to choose their preferred format for saving and loading financial
  data.
- Studies were conducted on those libraries from external resources like U tube, chat gpt, websites, etc...
- Making changes within functions to enable interactions between functions

## Additional Information
-----------------
- Make sure your device has python installed before running this program.
- Make sure your device has installed csv, sys,calender,os and re libraries before running this program. 
- For improved code organization, this program's functionalities are modularized and financial entries are stored on a list.
- Unexpected user inputs and file-related problems are handled properly through the implementation of error handling.

