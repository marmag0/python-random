#!/usr/bin/env python3

# Bucket Sort distributes elements into several buckets based on value ranges:
# - Each element is placed into a bucket corresponding to its value range
# - Each bucket is then sorted individually (using insertion sort, quicksort, or any efficient sorting algorithm)
# After sorting, all buckets are concatenated in order to produce the final sorted array
# This method works best when input is uniformly distributed over a known range, resulting in near-linear performance.

def bucketSort(arr, l):
    buckets = [[] for _ in range(10)]
    
    for i in range(l):
        if arr[i] < 0.1:
            buckets[0].append(arr[i])
        elif arr[i] < 0.2:
            buckets[1].append(arr[i])
        elif arr[i] < 0.3:
            buckets[2].append(arr[i])
        elif arr[i] < 0.4:
            buckets[3].append(arr[i])
        elif arr[i] < 0.5:
            buckets[4].append(arr[i])
        elif arr[i] < 0.6:
            buckets[5].append(arr[i])
        elif arr[i] < 0.7:
            buckets[6].append(arr[i])
        elif arr[i] < 0.8:
            buckets[7].append(arr[i])
        elif arr[i] < 0.9:
            buckets[8].append(arr[i])
        elif arr[i] < 1.0:
            buckets[9].append(arr[i])
        else:
            raise ValueError("Element out of range [0.0, 1.0)")
        
        for bucket in buckets:
            bucket.sort()

    index = 0
    for bucket in buckets:
        for value in bucket:
            arr[index] = value
            index += 1

def main():
    array = [0.15, 0.54, 0.94, 0.01, 0.44, 0.63]
    length = len(array)

    bucketSort(array, length)
    print(array)

if __name__ == "__main__":
    main()