import statistics as stats
import math as m

def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    total = 0
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

def test(data: list[int]):    

#  New Calculations for TLAB2: using the stats function to calculate mean/med/range, and variance
    list_average = stats.mean(data)
    print(round(list_average, 2))

    list_median = stats.median(data)
    print(round(list_median, 2))

    list_range = range(data)
    print(round(list_range, 2))

    stats.variance(data)
    var1 = stats.variance(data)
    print("{:.2f}".format(var1))

    m.sqrt(var1)
    stand_dev = m.sqrt(var1)
    print("{:.2f}".format(stand_dev))

    