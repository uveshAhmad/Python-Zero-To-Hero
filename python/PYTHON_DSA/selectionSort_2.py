def selection_sort_desc(arr):
    n = len(arr)

    # Traverse through all elements in the list
    for i in range(n):
        # Find the maximum element in the unsorted part
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j

        # Swap the found maximum element with the last element in the unsorted part
        arr[i], arr[max_index] = arr[max_index], arr[i]

# Example usage:
unsorted_list = [64, 34, 25, 12, 22, 11, 90]

print("Unsorted List:", unsorted_list)

selection_sort_desc(unsorted_list)

print("Sorted List (Descending with Max Element at the End):", unsorted_list)
