import csv

# Define the file path
file_path = 'NHANES_data_stroke_train.csv'

# Define the function to count occurrences of specified values in the last column
def count_last_column(file_path, value):
    count = 0
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            if int(row[-1]) == value:
                count += 1
    return count

# Count occurrences of values 1 and 2 in the last column
count_1 = count_last_column(file_path, 1)
count_2 = count_last_column(file_path, 2)

# Print the counts
print("Count of '1' in the last column:", count_1)
print("Count of '2' in the last column:", count_2)
print(count_1 / count_2)