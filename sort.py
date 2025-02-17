# sorts.py

import time


def bubble_sort(arr):
    """
    Bubble Sort: Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
    This process repeats until the list is sorted.
    """
    n = len(arr)
    print("\nStarting Bubble Sort")
    for i in range(n):
        swapped = False  # To check if any swap happened in this pass
        print(f"\nPass {i+1}:")
        for j in range(0, n - i - 1):
            print(f"  Comparing arr[{j}]={arr[j]} and arr[{j+1}]={arr[j+1]}")
            if arr[j] > arr[j + 1]:
                print(f"  -> Swapping {arr[j]} and {arr[j+1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print("  Array now:", arr)
                time.sleep(0.5)  # Slow down to observe the step-by-step changes
        if not swapped:
            # If no elements were swapped, the array is already sorted.
            print("  No swaps occurred in this pass. Array is sorted.")
            break
    return arr


def insertion_sort(arr):
    """
    Insertion Sort: Builds the sorted list one element at a time.
    It takes each element and inserts it into its correct position in the already-sorted part of the array.
    """
    print("\nStarting Insertion Sort")
    for i in range(1, len(arr)):
        key = arr[i]
        print(f"\nInserting element {key} at index {i}")
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key to one position ahead.
        while j >= 0 and key < arr[j]:
            print(f"  {key} < arr[{j}]={arr[j]}, shifting {arr[j]} to the right")
            arr[j + 1] = arr[j]
            j -= 1
            print("  Array now:", arr)
            time.sleep(0.5)
        arr[j + 1] = key
        print(f"Inserted {key} at position {j + 1}")
        print("  Array after insertion:", arr)
    return arr


def selection_sort(arr):
    """
    Selection Sort: Divides the array into a sorted and unsorted part.
    It repeatedly selects the smallest (or largest) element from the unsorted part and moves it to the sorted part.
    """
    n = len(arr)
    print("\nStarting Selection Sort")
    for i in range(n):
        min_idx = i
        print(f"\nSelecting minimum for position {i}")
        # Find the minimum element in the remaining unsorted array.
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                print(
                    f"  Found new minimum: arr[{j}]={arr[j]} < arr[{min_idx}]={arr[min_idx]}"
                )
                min_idx = j
        # Swap the found minimum element with the first element of the unsorted part.
        if min_idx != i:
            print(f"  Swapping arr[{i}]={arr[i]} with arr[{min_idx}]={arr[min_idx]}")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print("  Array now:", arr)
            time.sleep(0.5)
        else:
            print("  No swapping needed; current element is already the minimum")
    return arr


def merge_sort(arr):
    """
    Merge Sort: A divide and conquer algorithm that divides the array into halves,
    recursively sorts each half, and then merges the sorted halves.
    """
    print(f"\nMerge Sort called on {arr}")
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves.
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the two sorted halves.
    merged = merge(left_half, right_half)
    print(f"Merged {left_half} and {right_half} into {merged}")
    time.sleep(0.5)
    return merged


def merge(left, right):
    """
    Helper function for merge_sort that merges two sorted lists into one sorted list.
    """
    merged = []
    i = j = 0
    # Compare each element from left and right lists and append the smaller one.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            print(f"  Taking {left[i]} from left")
            i += 1
        else:
            merged.append(right[j])
            print(f"  Taking {right[j]} from right")
            j += 1
        time.sleep(0.5)
    # Append any remaining elements.
    while i < len(left):
        merged.append(left[i])
        print(f"  Appending remaining {left[i]} from left")
        i += 1
        time.sleep(0.5)
    while j < len(right):
        merged.append(right[j])
        print(f"  Appending remaining {right[j]} from right")
        j += 1
        time.sleep(0.5)
    return merged


def quick_sort(arr):
    """
    Quick Sort: An efficient divide and conquer algorithm that picks an element as pivot and partitions the array around the pivot.
    This implementation uses recursion to sort the partitions.
    """
    # Base case: arrays with less than 2 elements are already sorted.
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    print(f"\nQuick Sort called on {arr}")
    print(f"Pivot selected: {pivot}")
    # Partition the array into two sub-arrays:
    # - left: elements less than the pivot
    # - right: elements greater than or equal to the pivot
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    print(f"  Left partition (elements < pivot): {left}")
    print(f"  Right partition (elements >= pivot): {right}")
    time.sleep(0.5)

    # Recursively apply quick_sort on the partitions and combine the results.
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)
    combined = sorted_left + [pivot] + sorted_right
    print(f"Combined sorted parts: {combined}")
    time.sleep(0.5)
    return combined
