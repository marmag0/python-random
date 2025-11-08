#!/usr/bin/env python3

# Iterating through the list, taking one element at a time, and inserting it into its correct position 
# in the already sorted portion of the list. This is done by shifting larger elements to the right.

def insertionSort(arr, l):
       if l <= 1:
            return
       for i in range(1, l):
            key = 0
            while key < i:
                if arr[i] >  arr[key]:
                    key+=1
                    continue
                else:
                    break
            arr[key], arr[i] = arr[i], arr[key]
                 
def main():
    array = [1, 4, 5, 3, 9, 4]
    length = len(array)

    insertionSort(array, length)
    print(array)

if __name__ == "__main__":
    main()