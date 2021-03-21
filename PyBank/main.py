# PyBank

import csv
import os

# Load files

absolute_path = "C:\\Users\\Matija\\Desktop\\Personal_Projects\\Homework_3\PyBank"

file_to_load = os.path.join(absolute_path, "Resources", "budget_data.csv")
file_to_output = os.path.join(absolute_path, "analysis", "budget_analysis.txt")

total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999]
total_net = 0

with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)

    # Extract first row
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    # For each row in the reader
    for row in reader:

        # Track the total
        total_months += 1
        total_net += int(row[1])

        # Track net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

        # Calculate greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate average net change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# Generate Output summary
output = (
    f"Financial Analysis\n"
    f"------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print output to terminal
print(output)

# Export results to text file
with open(file_to_output, "w") as txt_file:
        txt_file.write(output)