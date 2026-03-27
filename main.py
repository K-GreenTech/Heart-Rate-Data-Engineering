from data_cleaning import clean_heartrate_data
from statistical import average, median, range, test

def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """
    data = []

    # open file using file I/O and read it into the `data` list
    file_object = open(file)

    for line in file_object:
        data.append(line.strip())        

    # Use `clean_heartrate_data` to clean the data and remove invalid entries
    cleaned_list = clean_heartrate_data(data) 

    # calculate the average, median, and range of this file using the functions you've wrote
    avg = average(cleaned_list)
    med = median(cleaned_list)
    ran = range(cleaned_list)
    test(cleaned_list)

    # print out your data quality measure to the console
    # print(file)
    # Not sure what to put here...

    # print out your descriptive statistics to the console
    # print("Average: ", avg)
    # print("Median: ", med)
    # print("Range: ", ran)

if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
