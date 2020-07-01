# Modules
import os
import csv

# Set path for file
budget_data = os.path.join('Resources/budget_data.csv')

# Track various financial parameters
total_months = 0
net_profit_total = 0
previous_value = 0
net_change = 0
net_change_list = []
total_net_change = 0
greatest_increase_month = ""
greatest_decrease_month = ""
greatest_increase = 0
greatest_decrease = 999

with open(budget_data, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    first_row = next(csvreader)
    total_months = total_months + 1
    net_profit_total = net_profit_total + float(first_row[1])
    previous_value = int(first_row[1])

    for row in csvreader:

        # Count row numbers for total months
        total_months = total_months +1
        
        # Net total amount of profit/loss over the entire period
        net_profit_total = net_profit_total + float(row[1])
        
        # Setting up average change calculation
        net_change = float(row[1]) - previous_value
        net_change_list = net_change_list + [net_change]
        total_net_change = total_net_change + net_change
        previous_value = float(row[1])

        # Obtaining Greatest increase and decrease values
        if net_change > greatest_increase:
            greatest_increase_month = row[0] 
            greatest_increase = net_change

        if net_change < greatest_decrease:
            greatest_decrease_month = row[0]
            greatest_decrease = net_change

    # calculate the average of the changes
    average_changes = total_net_change / len(net_change_list)
    
    #format data decimals
    formatted_net_profit_total = "{:.0f}".format(net_profit_total)
    formatted_average_changes = "{:.2f}".format(average_changes)
    formatted_greatest_increase = "{:.0f}".format(greatest_increase)
    formatted_greatest_decrease = "{:.0f}".format(greatest_decrease)

    print("                                                            ")
    print("Financial Analysis")
    print("------------------------------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${formatted_net_profit_total}")
    print(f"Average Change: ${formatted_average_changes}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} $({formatted_greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} $({formatted_greatest_decrease})")
    print("                                                            ")