def find_subsets(nums):
    def backtrack(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    nums.sort()
    result = []
    backtrack(0, [])
    return result

nums = list(map(int, input("Enter space-separated positive integers: ").split()))

all_subsets = find_subsets(nums)

print("All subsets:")
for subset in all_subsets:
    print(subset)
