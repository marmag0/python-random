#!/usr/bin/env python3

# Radix Sort processes each digit of the numbers starting from the least significant digit (LSD) to the most significant digit (MSD):
# - In each pass, the list is sorted based on the current digit using a stable sorting algorithm (commonly Counting Sort)
# - Elements are grouped into buckets based on their current digit and reassembled after each pass
# The process is repeated for each digit place until all digits have been processed
# This results in a fully sorted array in linear time relative to the number of digits.

def radixSort(arr, l):
    max_length = 0
    for i in range(l):
        arr[i] = str(arr[i])
        if len(arr[i]) > max_length:
            max_length = len(arr[i])

    for digit in range(max_length):
        counting = [0] * 10
        output = [''] * l

        for i in range(l):
            index = int(arr[i][-1 - digit]) if digit < len(arr[i]) else 0
            counting[index] += 1

        for i in range(1, 10):
            counting[i] += counting[i - 1]

        for i in range(l - 1, -1, -1):
            index = int(arr[i][-1 - digit]) if digit < len(arr[i]) else 0
            output[counting[index] - 1] = arr[i]
            counting[index] -= 1

        for i in range(l):
            arr[i] = output[i]
    
def main():
    array = [121, 432, 511, 372, 949, 404]
    length = len(array)

    radixSort(array, length)
    print(array)

if __name__ == "__main__":
    main()