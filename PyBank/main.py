# Import OS and import CSV
import os
import csv

column_index = 0
non_blank_row_count = 0

# Initialize the sum variables
total_sum = 0
change_sum = 0

# Set path for file
file_path = '/Users/santoshpoudel/Desktop/University_of_Toronto/Assignments/Python Assignment/python-challenge/PyBank/Resources/budget_data.csv'

# Count number of months (in column 1) - non_blank_rows and Sum values in column 2
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    for row in csv_reader:
        if row[column_index].strip():
            non_blank_row_count += 1
        value = float(row[1])
        total_sum += value

# Open the CSV file
with open(file_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Skip the header row
    next(csv_reader)
    
    # Store the rows in a list
    rows = list(csv_reader)

# Initialize variables
change_count = 0
previous_value = float(rows[0][1])
max_increase = 0
max_decrease = 0
max_increase_month = ""
max_decrease_month = ""

# Iterate through the rows and calculate the sum and count of changes
for row in rows:
    value = float(row[1])
    if change_count != 0:
        change = value - previous_value
        change_sum += change
        if change > max_increase:
            max_increase = change
            max_increase_month = row[0]
        if change < max_decrease:
            max_decrease = change
            max_decrease_month = row[0]
    previous_value = value
    change_count += 1

# Calculate the average change
average_change = change_sum / (change_count - 1)

# Print title for answer table
print("Financial Analysis")
print("-----------------------------")

# Print total month
print("Total Month:", non_blank_row_count)

# Print Total Value
print("Total :", total_sum)

# Print Average Change
print("Average Change:", average_change)

# Print Greatest Increase in Profits
print("Greatest Increase in Profits:", max_increase_month, "($", max_increase, ")")

# Print Greatest Decrease in Profits
print("Greatest Decrease in Profits:", max_decrease_month, "($", max_decrease, ")")

# Create a text file in the Analysis folder to add summary result
file_path = os.path.join('/Users/santoshpoudel/Desktop/University_of_Toronto/Assignments/Python Assignment/python-challenge/PyBank/Analysis', "PyBank_analysis.txt")

with open(file_path, "w") as file:
    # Write the analysis to the text file
    file.write("Financial Analysis\n")
    file.write("-----------------------------\n")
    file.write(f"Total Months: {non_blank_row_count}\n")
    file.write(f"Total: ${total_sum}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})\n")
    file.write(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n")

# Close the text file
file.close()