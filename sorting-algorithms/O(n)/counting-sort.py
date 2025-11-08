#!/usr/bin/env python3

# Counting Sort is a non-comparative sorting algorithm that works by counting the number of occurrences
# of each unique element in the input list:
# - A count array is created where the index represents the element value, and the value at that index represents the frequency of that element
# - The count array is used to place each element in its correct position in the output array
# After processing the count array, the elements are placed back in sorted order in the original array.
# This process results in a stable sort with a time complexity of O(n + k), where n is the number of elements and k is the range of the input.

def countingSort(arr, l):
    max_v = arr[0]
    min_v = arr[0]

    for i in range(1, l):
        if arr[i] > max_v:
            max_v = arr[i]
        if arr[i] < min_v:
            min_v = arr[i]

    counting = [0 for i in range(max_v-min_v+1)]

    for i in range(l):
        counting[arr[i]-1] += 1

    key = 0
    for i in range(len(counting)):
        for _ in range(counting[i]):
            arr[key] = min_v + i
            key += 1

def main():
    array = [1, 4, 5, 3, 9, 4]
    length = len(array)

    countingSort(array, length)
    print(array)

if __name__ == "__main__":
    main()