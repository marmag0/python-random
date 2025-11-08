#!/usr/bin/env python3

# Iterating through the list and repeatedly swapping adjacent elements if they are in the wrong order, 
# gradually "bubbling" larger elements to the end of the list.

def bubbleSort(arr, l):
    for i in range(0, l):
        for j in range(0, l-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                continue

def main():
    array = [1, 4, 5, 3, 9, 4]
    length = len(array)

    bubbleSort(array, length)
    print(array)

if __name__ == "__main__":
    main()


