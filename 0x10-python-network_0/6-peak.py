#!/usr/bin/python3
# Finds a peak in a list of unsorted integers
def find_peak(list_of_integers):
    array = list_of_integers

    left, right = 0, len(array) - 1

    while left <= right:
        mid = left + ((right - left) // 2)

        # check if left neighbor is greater
        if mid > 0 and array[mid] < array[mid - 1]:
            right = mid - 1
        # check if right neighbor is greater
        elif mid < len(array) - 1 and array[mid] < array[mid + 1]:
            left = mid + 1
        else:
            return array[mid]
