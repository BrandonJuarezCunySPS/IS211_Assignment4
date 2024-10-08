import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order

    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found


def binary_search_iterative(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


def binary_search_recursive(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)


def time_search_function(search_function, a_list, item):
    """Times the search function and returns the time taken and the result."""
    start_time = time.time()
    result = search_function(a_list, item)
    time_taken = time.time() - start_time
    return time_taken, result


if __name__ == "__main__":
    """Main entry point"""
    sizes = [500, 1000, 5000]
    search_item = 99999999  # Item we know does not exist
    search_functions = {
        "Sequential Search": sequential_search,
        "Ordered Sequential Search": ordered_sequential_search,
        "Binary Search Iterative": binary_search_iterative,
        "Binary Search Recursive": binary_search_recursive,
    }

    for the_size in sizes:
        print(f"\nSearching in lists of size {the_size}:")
        for name, search_function in search_functions.items():
            total_time = 0
            for _ in range(100):
                mylist = get_me_random_list(the_size)
                if name != "Sequential Search":
                    mylist.sort()  # Sort the list for binary and ordered searches

                time_spent, _ = time_search_function(search_function, mylist, search_item)
                total_time += time_spent

            avg_time = total_time / 100
            print(f"{name} took {avg_time:10.7f} seconds to run, on average")