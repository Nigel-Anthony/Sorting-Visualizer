# main.py

import random
import time
from sort import bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort


def print_menu():
    print("\nSorting Visualizer")
    print("------------------")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Selection Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Exit")


def get_user_choice():
    choice = input("\nSelect a sorting algorithm (1-6): ")
    return choice.strip()


def get_array():
    # Ask user whether to input an array manually or generate a random one.
    method = input(
        "\nDo you want to (1) input an array or (2) generate a random array? Enter 1 or 2: "
    ).strip()
    if method == "1":
        arr_str = input("Enter numbers separated by spaces: ")
        # Convert the input string to a list of integers.
        arr = list(map(int, arr_str.split()))
    else:
        size = int(input("Enter the size of the random array: "))
        max_val = int(input("Enter the maximum value for elements: "))
        arr = [random.randint(1, max_val) for _ in range(size)]
        print("Generated array:", arr)
    return arr


def main():
    while True:
        print_menu()
        choice = get_user_choice()

        if choice == "6":
            print("Exiting the Sorting Visualizer. Goodbye!")
            break

        arr = get_array()
        # Make a copy of the array for sorting (if needed) so that original input is preserved.
        original_arr = arr.copy()

        # Choose the appropriate sorting function based on the user's selection.
        if choice == "1":
            sorted_arr = bubble_sort(arr)
        elif choice == "2":
            sorted_arr = insertion_sort(arr)
        elif choice == "3":
            sorted_arr = selection_sort(arr)
        elif choice == "4":
            print("\nNote: Merge Sort will display recursive merging steps.")
            sorted_arr = merge_sort(arr)
        elif choice == "5":
            sorted_arr = quick_sort(arr)
        else:
            print("Invalid choice. Please try again.")
            continue

        print("\nOriginal array:", original_arr)
        print("Sorted array:", sorted_arr)

        # Pause before showing the menu again.
        time.sleep(1)


if __name__ == "__main__":
    main()
