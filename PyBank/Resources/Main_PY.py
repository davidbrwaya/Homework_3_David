# Modules
import os
import csv
from pathlib import Path

# Set path for file
csvpath = os.path.join("budget_data.csv")
total = 0
total_month = 0
average_change = 0
greatest_increase = ["",0]
greatest_decrease = ["",0]
current_value = 0
previous_value = 0
total_change = 0
change = 0

# Empty List to contain the change of each row
change_list=[]

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    #For loop is looping through budget_data
    for row in csvreader:
        current_value = int(row[1])
        change = current_value - previous_value
        previous_value = current_value
        total_change += change
        #Change being added to change list
        change_list += [change]
        total_month = total_month + 1
        total = total + int(row[1])
        average_change = sum(change_list) / total_month
        if change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = change
        if change < greatest_decrease[1]:
            greatest_decrease[0] = row[0] 
            greatest_decrease[1] = change


    

#Print results
print(f"Total Months:" , total_month) 
print(f"Total: $" , total)
print(f"Average Change:" , average_change)
print(f"Greatest Increase in Profits:" , greatest_increase) 
print(f"Greatest Decrease in Profits:" , greatest_decrease)



# Output files
output_file = Path("Financial_Analysis_Summary.txt")

with open(output_file,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {total_month}")
    file.write("\n")
    file.write(f"Total: ${total_change}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(change_list)/len(change_list),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase}[1])")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${(greatest_decrease)}[1])")
