'''---------------------------------------------------------------------------------------------------------------------------------------------
Problem Statement : Implement a problem of move all zeroes to end of array.
                    - Given an array of random numbers, Push all the zero’s of a given array to the end of the array. For example, if the given
                      arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order of all other elements should be same.
---------------------------------------------------------------------------------------------------------------------------------------------'''


def move_zeros_to_end(arr):
    non_zero_count = 0

    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_count], arr[i] = arr[i], arr[non_zero_count]
            non_zero_count += 1

arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
move_zeros_to_end(arr)
print(arr)
