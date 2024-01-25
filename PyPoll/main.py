# Import OS and CSV file
import os
import csv

column_index = 0
count_ballotID = 0

#  Set file path for the CSV file - PyPoll
file_path = '/Users/santoshpoudel/Desktop/University_of_Toronto/Assignments/Python Assignment/python-challenge/PyPoll/Resources/election_data.csv'

# Count total number of Vote Cast by Voters
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    for row in csv_reader:
        if row[column_index].strip():
            count_ballotID += 1

# Calculate total votes received by each candidate
def calculate_frequency(csv_reader):
    from collections import Counter
    unique_name = Counter()

    for row in csv_reader:
        name = row[2]  # Column C
        unique_name[name] += 1
    
    return unique_name

## Count Total  (Frequency) each Candidate name appeared next to Ballot ID
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    result = calculate_frequency(csv_reader)

# Calculate Percentage of Total Votes each Candidates secured.
    percent_dict = {}
    for name, frequency in result.items():
        percentage = (frequency / count_ballotID) * 100
        percent_dict[name] = percentage
    
# Find the winning candidate who has the highest percentage of vote count
winning_candidate = max(percent_dict, key=percent_dict.get)

# Print results
print("Election Results")
print("---------------------------------------------")
print("\n")
print("Total Votes : ", count_ballotID)
print("---------------------------------------------")
print("\n")
# Print the percentage and vote count for each candidate
for name, frequency in result.items():
    percentage = percent_dict[name]
    print(f"{name}: {percentage:.3f}% ({frequency})")

print("---------------------------------------------")

print("Winner : ", winning_candidate)

# Create a text file in the Analysis folder to add summary result

file_path = os.path.join('/Users/santoshpoudel/Desktop/University_of_Toronto/Assignments/Python Assignment/python-challenge/PyPoll/Analysis', "PyPoll_analysis.txt")

with open(file_path, "w") as file:
    # Write the analysis to the text file
    file.write("Election Results\n")
    file.write("---------------------------------------------\n") 
    file.write(f"Total Votes: {count_ballotID}\n")
    file.write("-----------------------------\n")
    for name, frequency in result.items():
            percentage = percent_dict[name]
            file.write(f"{name}: {percentage:.3f}% ({frequency})\n")
    
    file.write(f"Winner: {winning_candidate}\n")

# Close the text file
    file.close()





    

