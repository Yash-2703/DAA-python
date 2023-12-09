'''---------------------------------------------------------------------------------------------------------------------------------------------
Problem Statement: Implement a problem of number of zeroes.
                    -Given an array of 1s and 0s which has all 1s first followed by all 0s? Find the number of 0s.
                     Count the number of zeroes in the given array.
---------------------------------------------------------------------------------------------------------------------------------------------'''


def count_zeros(arr, left, right):
    if arr[right] == 1:
        return 0
    if arr[left] == 0:
        return right - left + 1

    mid = (left + right) // 2
    return count_zeros(arr, left, mid) + count_zeros(arr, mid + 1, right)

arr = [1, 1, 1, 1, 0, 0, 0, 0, 0]
count = count_zeros(arr, 0, len(arr) - 1)
print("Number of zeros:", count)
