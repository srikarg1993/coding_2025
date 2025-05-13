#Grokking Algorithms
"""
Collection of functions to test each and every concept learnt as part of the Grokking algorithms textbook

Author: Srikar Gunisetty
Date:   05/12/2025
"""

def binary_search(list, item):
    """
    function to find 
    
    Precondition for list: sorted array of intezers
    item                 : integer to look up in the list
    """
    low = 0
    high = len(list)-1
    while low <= high:
        guess = (low+high) // 2
        if list[guess] == item:
            return guess
        elif list[guess] > item:
            high = guess-1
        else:
            low = guess + 1
    return None

# Selection sort - ascending
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort_asc(arr):
    sorted_array_asc = []
    for i in range(len(arr)):
        smallest_element_index = find_smallest(arr)
        sorted_array_asc.append(arr.pop(smallest_element_index))
    return sorted_array_asc


# Selection sort - descending
def find_largest(arr):
    largest = arr[0]
    largest_index = 0
    for i in range(1,len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            largest_index = i
    return largest_index

def selection_sort_desc(arr):
    sorted_arr_desc = []
    for i in range(len(arr)):
        largest_element_index = find_largest(arr)
        sorted_arr_desc.append(arr.pop(largest_element_index))
    return sorted_arr_desc

selection_sort_asc([4,3,2,1])
# selection_sort_desc([1,2,3,4])
        
        
