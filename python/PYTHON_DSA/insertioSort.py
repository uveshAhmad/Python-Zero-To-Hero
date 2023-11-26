def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be compared
        j = i - 1  # Index of the previous element

        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key at its correct position in sorted part
        arr[j + 1] = key

# Example usage:
my_list = [12, 11, 13, 5, 6]
insertion_sort(my_list)
print("Sorted array:", my_list)
