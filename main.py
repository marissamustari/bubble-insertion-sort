# Project No.: 6
# Author: Marissa Mustari
# Description: A program that compares time performances using bubble and insertion sorts and displays them in a graph

import random
import time
import sys
import matplotlib.pyplot as plt

# Sets recursion limit
sys.setrecursionlimit(2000)

# Bubble sort
def bubble_sort(int_array, n=None):
    if n is None:
        n = len(int_array)
    if n == 1:
        return int_array

    for i in range(n - 1):
        if int_array[i] > int_array[i + 1]:
            int_array[i], int_array[i + 1] = int_array[i + 1], int_array[i]

    return bubble_sort(int_array, n - 1)

# Insertion sort
def insertion_sort(int_array, n=None):
    if n is None:
        n = len(int_array)
    if n <= 1:
        return int_array

    insertion_sort(int_array, n - 1)
    last_val = int_array[n - 1]
    j = n - 2
    while j >= 0 and int_array[j] > last_val:
        int_array[j + 1] = int_array[j]
        j -= 1
    int_array[j + 1] = last_val
    return int_array

# Sorts time and returns difference
def sort_time(sort_funct, int_array):
    start_time = time.perf_counter()
    sort_funct(int_array.copy())
    end_time = time.perf_counter()
    time_diff = end_time - start_time
    return time_diff

# Main function to create random list of integers
def main():
    list_lens = [10, 50, 100, 500, 1000]
    sorted_list = []

    for length in list_lens:
        original_list = [random.randint(1, length) for _ in range(length)]

        bubble_time = sort_time(bubble_sort, original_list)
        insertion_time = sort_time(insertion_sort, original_list)

        sorted_list.append((length, bubble_time, insertion_time))

    # Prints results
    print(f"{'Length':<10}{'Bubble Time':<20}{'Insertion Time'}")
    print("-" * 50)
    for length, bubble_time, insertion_time in sorted_list:
        print(f"{length:<10}{bubble_time:<20.6e}{insertion_time:.6e}")

    # For plotting
    lengths = [x[0] for x in sorted_list]
    bubble_times = [x[1] for x in sorted_list]
    insertion_times = [x[2] for x in sorted_list]

    plt.plot(lengths, bubble_times, marker='o', label='Bubble Sort')
    plt.plot(lengths, insertion_times, marker='s', label='Insertion Sort')

    plt.xlabel('List Size (N)')
    plt.ylabel('Time (seconds)')
    plt.title('Recursive Bubble vs Insertion Sort Performance')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

main()
