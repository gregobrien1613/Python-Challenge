import os
import csv

# Path to collect data from the Resources folder
bank_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

# Read in the CSV file
with open(bank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skips Header
    next(csvreader)

    # Declares row counter variable
    counter = 0

    # Counts the sum
    total = 0

    # Declares variable to find greatest increase
    greatestInc = 0

    # Declares variable to find greatest Decrease
    greatestDec = 0

    # Loop through the data
    for row in csvreader:

        # Adds to the total for each row
        total = total + int((row[1]))

        # Counts the rows (Dates)
        counter += 1

        # If profit is greater than previous profits update greatestInc variable
        if int(row[1]) > int(greatestInc):
            greatestInc = row[1]

        # If profit is less than previous profits update greatestDec variable
        if int(row[1]) < int(greatestDec):
            greatestDec = row[1]

        #Puts date for greatestInc
        if int(row[1]) == int(greatestInc):
            incLineNumber = row[0]

        # Puts date for greatestDec
        if int(row[1]) == int(greatestDec):
            decLineNumber = row[0]

# Declares variable for average profit/loss
average = "{:,.2f}".format(float(total / counter))

# Reformats float values
total = "{:,.2f}".format(float(total))
greatestInc = "{:,.2f}".format(float(greatestInc))
greatestDec = "{:,.2f}".format(float(greatestDec))

# Prints things in terminal
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {counter}")
print(f"Total: ${total}")
print(f" Average Change: ${average}")
print(f"Greatest Increase: {incLineNumber} ${greatestInc}")
print(f"Greatest Decrease: {decLineNumber} ${greatestDec}")

# Creates csv file
f= open("pyBank.txt","w+")

# Writes things into csv file
f.write("Financial Analysis\n")
f.write("---------------------\n")
f.write(f"Total Months: {counter} and sum is {total}\n")
f.write(f"Total: ${total}\n")
f.write(f" Average Change: ${average}\n")
f.write(f"Greatest Increase: {incLineNumber} ${greatestInc}\n")
f.write(f"Greatest Decrease: {decLineNumber} ${greatestDec}\n")
f.close()
