#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """A function that finds a peak in a list of unsorted integers"""

    array = list_of_integers

    if not array:
        return None

    if len(array) == 1:
        return array[0]

    if len(array) == 2:
        return max(array[0], array[1])

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
