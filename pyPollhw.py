import os
import csv

# Used to find max value
import operator

# Path to collect data from the Resources folder
bank_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

# Read in the CSV file
with open(bank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skips the header
    next(csvreader)

    # Declares row counter variable
    counter = 0

    # Declares how many votes Khan got
    KhanCount = 0

    # Declares how many votes Correy got
    CorreyCount = 0

    # Declares how many votes Li got
    LiCount = 0

    # Declares how many votes O'Tooley got
    TooleyCount = 0

    # For loop goes through csv
    for row in csvreader:

        # Updates counter variable
        counter += 1

        # If voter voted Khan add to KhanCount
        if row[2] == "Khan":
            KhanCount += 1

        # If voter voted Correy add to CorreyCount
        if row[2] == "Correy":
            CorreyCount += 1

        # If voter voted Li add to LiCount
        if row[2] == "Li":
            LiCount += 1

        # If voter voted O'Toooley add to TooleyCount
        if row[2] == "O'Tooley":
            TooleyCount += 1

# Prints everything
print("Poll Analysis\n---------------------")
print(f"Total Votes: {counter}")
print(f"Khan: %{KhanCount / counter * 100} ({KhanCount})")
print(f"Correy: %{CorreyCount / counter * 100} ({CorreyCount})")
print(f"Li: %{LiCount / counter * 100} ({LiCount})")
print(f"O'Tooley: %{TooleyCount / counter * 100} ({TooleyCount})")

# Creates Dictionary with vote counts
candidates = {"Khan": KhanCount, "O'Tooley": TooleyCount, "Li": LiCount, "Correy": CorreyCount}

#Gets the max value of dictionary and prints the item
keyMax = max(candidates.items(), key = operator.itemgetter(1))[0]
print(f"--------------\nWinner is: {keyMax}")

# Creates csv
f= open("pyPollhw.txt","w+")

#Puts info into csv
f.write("Poll Analysis\n---------------------")
f.write(f"Total Votes: {counter}\n")
f.write(f"Khan: %{KhanCount / counter * 100} ({KhanCount}\n)")
f.write(f"Correy: %{CorreyCount / counter * 100} ({CorreyCount})\n")
f.write(f"Li: %{LiCount / counter * 100} ({LiCount})\n")
f.write(f"O'Tooley: %{TooleyCount / counter * 100} ({TooleyCount})\n")
f.write(f"--------------\nWinner is: {keyMax}")
f.close()
