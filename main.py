def move_zeros_to_end(arr):
    non_zero_count = 0

    # Iterate through the array, moving non-zero elements to the front.
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_count], arr[i] = arr[i], arr[non_zero_count]
            non_zero_count += 1

# Example usage:
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
move_zeros_to_end(arr)
print(arr)