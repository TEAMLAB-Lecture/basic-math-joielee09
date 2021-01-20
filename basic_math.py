#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""


def get_greatest(number_list):
    greatest_number = max(number_list)
    return greatest_number


def get_smallest(number_list):
    smallest_number = min(number_list)
    return smallest_number


def get_mean(number_list):
    mean = sum(number_list)/len(number_list)
    return mean


def get_median(number_list):
    sortedList = sorted(number_list)
    l_len = len(number_list)
    if l_len%2:
        return sortedList[(l_len-1)//2]
    else:
        return (sortedList[(l_len-1)//2]+sortedList[(l_len-1)//2+1])/2.0
    return median
