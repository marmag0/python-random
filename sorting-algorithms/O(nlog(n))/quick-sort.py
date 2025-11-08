#!/usr/bin/env python3

# Recursively selecting a pivot element and partitioning the list into two sublists:
# - Elements smaller than the pivot are moved to the left
# - Elements greater than the pivot are moved to the right
# After partitioning, the pivot is placed in its final sorted position
# Then, the sublists (left and right of the pivot) are recursively sorted.

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while arr[i] < pivot and i < right:
            i+=1
        while arr[j] >= pivot and j > left:
            j-=1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i

def quickSort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quickSort(arr, left, partition_pos - 1)
        quickSort(arr, partition_pos + 1, right)

def main():
    array = [1, 4, 5, 3, 9, 4]

    quickSort(array, 0, len(array) - 1)
    print(array)

if __name__ == "__main__":
    main()