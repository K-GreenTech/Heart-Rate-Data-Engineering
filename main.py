from data_cleaning import clean_heartrate_data
from statistical import average, median, range
import statistics as stats

# def clean_heartrate_data(data: list) -> tuple:
#     """
#     Clean raw heart-rate data by removing malformed or impossible values.
#     """
#     cleaned_data = []
        
#     for item in data:   
#         if type(item) == str and item.isdigit():
#             cleaned_data.append(int(item))
#         if type(item) == int:
#             cleaned_data.append(item)
    
#     return cleaned_data

# def average(data: list) -> float:
#     """
#     Calculate average of a list of integers using a for-loop. Assumes data is clean.
#     """
#     total = 0
#     numbers = data
#     for num in data:
#         total += num
#     average = total / len(data)
#     print("Average: ", average)

# def median(data: list) -> float:
#     new_filtered = clean_heartrate_data(data)
#     len_lst = len(new_filtered)
#     sorted_HR_values = sorted(new_filtered)

#     if len_lst % 2 == 0:
#         index_pos_2 = int(len_lst/2)
#         index_pos_1 = index_pos_2 - 1
#         median = (sorted_HR_values[index_pos_2] + sorted_HR_values[index_pos_1])/2
#     else:
#         # return index_pos of median (middle value) in list
#         index_pos = (len_lst - 1 ) / 2
#         for i,value in enumerate(sorted_HR_values):
#             if i == index_pos:
#                 # if i == index_pos, then return median
#                 median = value
#     return median

# def range(data: list) -> float:
#     clean_heartrate_data(data)
    
#     x = max(data)
#     y = min(data)

#     difference = x - y
#     return difference    

# def rolling_avg(data: list, k: int) -> float:
#     """
#     CHALLENGE FUNCTION (Optional)
#     """
#     pass

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
 
    list_average = stats.mean(cleaned_list)
    print(list_average)

    list_median = stats.median(cleaned_list)
    print(list_median)

    list_range = range(cleaned_list)
    print(list_range)

    stats.variance(data)



    # print out your data quality measure to the console
    # print(file)
    # Not sure what to put here...

    # print out your descriptive statistics to the console
    print("Average: ", avg)
    print("Median: ", med)
    print("Range: ", ran)

if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
