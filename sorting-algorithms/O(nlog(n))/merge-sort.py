#!/usr/bin/env python3

# Recursively dividing the list into smaller sublists until each sublist has one element, 
# then merging the sublists back together in sorted order.

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        #recursion
        mergeSort(left_arr)
        mergeSort(right_arr)

        #merge
        l = 0
        r = 0
        i = 0

        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] >= right_arr[r]:
                arr[i] = right_arr[r]
                r+=1
            else:
                arr[i] = left_arr[l]
                l+=1
            i+=1
        
        if l < len(left_arr):
            while l < len(left_arr):
                arr[i] = left_arr[l]
                l += 1
                i += 1
        elif r < len(right_arr):
            while r < len(right_arr):
                arr[i] = right_arr[r]
                r += 1
                i += 1
    
    return arr

def main():
    array = [1, 4, 5, 3, 9, 4]

    mergeSort(array)
    print(array)

if __name__ == "__main__":
    main()