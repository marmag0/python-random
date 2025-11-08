#!/usr/bin/env python3

# Building a max heap from the unsorted list:
# - The largest element is moved to the root (index 0) of the heap
# - The heap property is maintained by rearranging elements
# After the max heap is built, the root element (maximum) is swapped with the last element
# The heap size is reduced, and the heap property is restored recursively
# This process repeats until all elements are sorted in ascending order.

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def shiftDown(arr, i, length):
    while True:
        l = 2*i + 1     #left child index
        r = 2*i + 2     #right child index
        largest = i     #largest assumption

        #check if left child exists and is greater than current largest
        if l < length and arr[l] > arr[largest]:
            largest = l

        #check if right child exists and is greater than current largest
        if r < length and arr[r] > arr[largest]:
            largest = r

        #if the largest is not the current node, swap and continue
        if largest != i:
            swap(arr, i, largest)
            i = largest
        else:
            break

def heapSort(arr):
    for j in range((len(arr)-2)//2, -1, -1):
        shiftDown(arr, j, len(arr))

    for end in range(len(arr)-1, 0, -1):
        swap(arr, 0, end)
        shiftDown(arr, 0, end)

def main():
    array = [1, 4, 5, 3, 9, 4]

    heapSort(array)
    print(array)

if __name__ == "__main__":
    main()