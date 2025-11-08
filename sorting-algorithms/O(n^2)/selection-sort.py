#!/usr/bin/env python3

# Iterating through the list and selecting the smallest (or largest) element from the unsorted part of the list, 
# then swapping it with the first unsorted element. This process repeats until the entire list is sorted.

def selectionSort(arr, l):
    for i in range(0, l):
        i_min = i
        for j in range (i+1, l):
            if arr[j] < arr[i_min]:
                i_min = j
            
        if i != i_min:
            arr[i], arr[i_min] = arr[i_min], arr[i]    

def main():
    array = [1, 4, 5, 3, 9, 4]
    length = len(array)

    selectionSort(array, length)
    print(array)

if __name__ == "__main__":
    main()