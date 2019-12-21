import os
import csv

# Path to collect data from the Resources folder
bank_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

# Read in the CSV file
with open(bank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    counter = 0
    total = 0
    greatestInc = 0
    greatestDec = 0
    # Loop through the data
    for row in csvreader:
        total = total + int((row[1]))
        counter += 1
        if int(row[1]) > int(greatestInc):
            greatestInc = row[1]
        if int(row[1]) < int(greatestDec):
                greatestDec = row[1]

        if int(row[1]) == int(greatestInc):
            incLineNumber = row[0]
        if int(row[1]) == int(greatestDec):
            decLineNumber = row[0]

average = float(total / counter)

print("Financial Analysis")
print("---------------------")
print(f"Total Months: {counter} and sum is {total}")
print(f"Total: ${total}")
print(f" Average Change: ${average}")
print(f"Greatest Increase: {incLineNumber} ${greatestInc}")
print(f"Greatest Decrease: {decLineNumber} ${greatestDec}")

f= open("pyBank.txt","w+")
f.write("Financial Analysis\n")
f.write("---------------------\n")
f.write(f"Total Months: {counter} and sum is {total}\n")
f.write(f"Total: ${total}\n")
f.write(f" Average Change: ${average}\n")
f.write(f"Greatest Increase: {incLineNumber} ${greatestInc}\n")
f.write(f"Greatest Decrease: {decLineNumber} ${greatestDec}\n")
f.close()
        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
