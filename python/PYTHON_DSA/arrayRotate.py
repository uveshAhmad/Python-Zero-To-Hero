def rotate_array_by_one(arr):
    n = len(arr)
    temp = arr[0]
    
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    
    arr[n - 1] = temp

# Example usage:
original_array = [1, 2, 3, 4, 5]
rotate_array_by_one(original_array)

print("Rotated array:", original_array)