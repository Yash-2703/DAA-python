'''---------------------------------------------------------------------------------------------------------------------------------------------
Problem Statement :Given a set of non-negative integers and a value sum, the task is to check if there is a subset of the
given set whose sum is equal to the given sum.
---------------------------------------------------------------------------------------------------------------------------------------------'''

def is_subset_sum(nums, target_sum):
    n = len(nums)

    dp = [[False for _ in range(target_sum + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if nums[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

    return dp[n][target_sum]

nums = [3, 34, 4, 12, 5, 2]
target_sum = 9
result = is_subset_sum(nums, target_sum)
if result:
    print("Subset with sum {} exists.".format(target_sum))
else:
    print("No subset with sum {} exists.".format(target_sum))
