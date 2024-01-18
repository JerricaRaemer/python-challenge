import os
import csv

# Set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    csvreader_iteration = next(csvreader)
    # print(f"CSV Reader Iteration: {csvreader_iteration}")

    profits = []
    date = []

    for row in csvreader:
        # print(row)
        profits.append(row[1])
        date.append(row[0])
    # print("List of Profits = ", profits)
    # print("List of dates = ", date)


    
    # get total number of months
    unique_count = len(set(date))
    # print("Total number of months = ", unique_count)
    
    # total amount of profits and losses
    profit_integers = [int(element) for element in profits]
    # print("Profit Integer List = ", profit_integers)
    total_amount = int(sum(profit_integers)) 
    # print("Total amount of profits and losses = ", total_amount)

    # Average difference of profits
    difference_profits = [profit_integers[i+1] - profit_integers[i] for i in range(len(profit_integers)-1)]
    # print("List of differences of profits between each element = ", difference_profits)
    average_difference = round((sum(difference_profits))/(len(difference_profits)),2)
    # print("The average profit is ", average_difference)

    # Greatest increase in profit
    max_profit = max(difference_profits)
    # print("The greatest increase in profits is $", max_profit)

    # Greatest decrease in profit
    min_profit = min(difference_profits)
    # print("The greatest decrease in profits is $", min_profit)

    # Get the dates
    index_max = difference_profits.index(max_profit)
    # print("Max Index Number =", index_max)
    max_date = date[index_max+1]
    # print("The date the maximum profit took place is ", max_date)

    index_min = difference_profits.index(min_profit)
    # print("Min Index Number =", index_min)
    min_date = date[index_min+1]
    # print("The date the minimum profit took place is ", min_date)

    # Python financial analysis
    print("Financial Analysis:")
    print("----------------------------")
    print("Total months: ", unique_count)
    print("Total: $", total_amount)
    print("Average Change: $", average_difference)
    print("Greatest Increase in Profits: ", max_date, "($", max_profit, ")")
    print("Greatest Decrease in Profits: ", min_date, "($", min_profit, ")")

    # open text file
    string_unique_count = str(unique_count)
    string_total_amount = str(total_amount)
    string_average_difference = str(average_difference)
    string_max_date = str(max_date)
    string_max_profit = str(max_profit)
    string_min_date = str(min_date)
    string_min_profit = str(min_profit)

    file = open("analysis/Financial_Analysis.txt", "w")
    file.write("Financial Analysis:")
    file.write("----------------------------\n")
    file.write("Total months: ")
    file.write(string_unique_count)
    file.write("\n")
    file.write("Total: $")
    file.write(string_total_amount)
    file.write("\n")
    file.write("Average Change: $")
    file.write(string_average_difference)
    file.write("\n")
    file.write("Greatest Increase in Profits: ")
    file.write(string_max_date)
    file.write(" ($")
    file.write(string_max_profit)
    file.write(")\n")
    file.write("Greatest Decrease in Profits: ")
    file.write(string_min_date)
    file.write(" ($")
    file.write(string_min_profit)
    file.write(")")


