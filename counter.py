import csv

# Path to your CSV file
csv_file_paths = ['RFpred.csv', 'GBTpred.csv', 'SVMpred.csv']

# Open and read the CSV file
for file in csv_file_paths:
    # Initialize counters
    count_above_05 = 0
    count_below_05 = 0
    with open(file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        # Loop through each row
        for row in csv_reader:
            # Convert Pred_Probability to float and compare
            if float(row['Pred_Probability']) >= 0.5:
                count_above_05 += 1
            elif float(row['Pred_Probability']) < 0.5:
                count_below_05 += 1

    # Print the results
    print(file)
    print(f"Number above 0.5: {count_above_05}")
    print(f"Number below 0.5: {count_below_05}\n")