from data_cleaning import clean_heartrate_data
import statistics as stats

def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    total = 0
    numbers = data
    for num in data:
        total += num
    average = total / len(data)
    print("Average: ", average)

def median(data: list) -> float:
    len_lst = len(data)
    sorted_HR_values = sorted(data)

    if len_lst % 2 == 0:
        index_pos_2 = int(len_lst/2)
        index_pos_1 = index_pos_2 - 1
        median = (sorted_HR_values[index_pos_2] + sorted_HR_values[index_pos_1])/2
    else:
        # return index_pos of median (middle value) in list
        index_pos = (len_lst - 1 ) / 2
        for i,value in enumerate(sorted_HR_values):
            if i == index_pos:
                # if i == index_pos, then return median
                median = value
    return median

def range(data: list) -> float:     
    x = max(data)
    y = min(data)

    difference = x - y
    return difference    

