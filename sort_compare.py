import argparse
# other imports go here

import random
import time

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list
    

def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
    end = time.time()
    return a_list, end - start


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


def shell_sort(a_list):
    """Perform shell sort on a_list and return the sorted list.

    :param a_list: List to be sorted
    :return: The sorted list
    """
    start = time.time()
    sublistcount = len(a_list) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(a_list, startposition, sublistcount)

        sublistcount = sublistcount // 2
    end = time.time()
    return a_list, end - start


def python_sort(a_list):
    """Use Python built-in sorted function as a wrapper.

    :param a_list: List to be sorted
    :return: The sorted list
    """
    start = time.time()
    sorted_list = sorted(a_list)
    end = time.time()
    return sorted_list, end - start


if __name__ == "__main__":
    """Main entry point"""
    list_sizes = [500, 1000, 5000]

    for the_size in list_sizes:
        mylist = get_me_random_list(the_size)

        # Benchmark Python's built-in sort
        sorted_list, time_taken = python_sort(mylist.copy())
        print(f"Python sort took {time_taken:10.7f} seconds to run, on average for a list of {the_size} elements")

        # Benchmark Insertion Sort
        sorted_list, time_taken = insertion_sort(mylist.copy())
        print(f"Insertion sort took {time_taken:10.7f} seconds to run, on average for a list of {the_size} elements")

        # Benchmark Shell Sort
        sorted_list, time_taken = shell_sort(mylist.copy())
        print(f"Shell sort took {time_taken:10.7f} seconds to run, on average for a list of {the_size} elements")