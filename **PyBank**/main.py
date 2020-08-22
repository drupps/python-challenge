# Modules
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
print(csvpath)
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

     # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    data = list(csvreader)
    #print(data)
    total = 0
    lastRow = 0
    totalChange = 0
    greatestIncrease = 0
    greatestDecrease = 0
    # Read each row of data after the header blah
    for row in data:
         
        total = (int(row[1]) + total)
        #print(total)

        months = len(data)
        #print(months)

        print(row)
      
        if lastRow == 0:
            lastRow = int(row[1])
        else:
            change = int(row[1]) - lastRow
            totalChange = totalChange + change
            lastRow = int(row[1])
            
            if change > greatestIncrease:
                greatestIncrease = change
                greatestMonth = (row[0])
            
            if change < greatestDecrease:
                greatestDecrease = change
                worstMonth = (row[0])
                
    #print(f'{greatestMonth} {greatestIncrease} {worstMonth} {greatestDecrease}')
    average = totalChange / (months-1)

    print(f'Financial Analysis \n----------------------------')
    print(f'Total Months: {months}')
    print(f'Total: ${total}')
    print(f'Average Change: ${average:.2f}')
    print(f'Greatest Increase in Profits: {greatestMonth} {greatestIncrease}')
    print(f'Greatest Decrease in Profits: {worstMonth} {greatestDecrease}') #add worst month

# Specify the file to write to
output_path = os.path.join("Analysis", "PyBank_Results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer

    csvfile.write(f'Financial Analysis \n----------------------------\n')
    csvfile.write(f'Total Months: {months}\n')
    csvfile.write(f'Total: ${total}\n')
    csvfile.write(f'Average Change: ${average:.2f}\n')
    csvfile.write(f'Greatest Increase in Profits: {greatestMonth} (${greatestIncrease})\n')
    csvfile.write(f'Greatest Decrease in Profits: {worstMonth} (${greatestDecrease})\n')
   