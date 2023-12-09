'''---------------------------------------------------------------------------------------------------------------------------------------------
Problem Statement :Given an array of integers arr[], The task is to find all its subsets.
The subset cannot contain duplicate elements, so any repeated subset should be considered only once in the output.
---------------------------------------------------------------------------------------------------------------------------------------------'''

def subsets(arr):
    def backtrack(start, path):
        result.append(path[:])

        for i in range(start, len(arr)):
            if i > start and arr[i] == arr[i - 1]:
                continue

            path.append(arr[i])
            backtrack(i + 1, path)
            path.pop()

    arr.sort()
    result = []
    backtrack(0, [])
    return result

arr = list(map(int, input("Enter space-separated integers for the array: ").split()))

all_subsets = subsets(arr)

print("All subsets without duplicate elements:")
for subset in all_subsets:
    print(subset)
