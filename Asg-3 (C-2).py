def is_subset_sum(nums, target_sum):
    n = len(nums)

    # Create a 2D table to store the results of subproblems
    dp = [[False for _ in range(target_sum + 1)] for _ in range(n + 1)]

    # If the target sum is 0, then an empty subset is always a solution
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the table using bottom-up dynamic programming
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            # If the current element is greater than the target sum, ignore it
            if nums[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # Include the current element or exclude it
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

    # The final result is stored in dp[n][target_sum]
    return dp[n][target_sum]

# Example usage:
nums = [3, 34, 4, 12, 5, 2]
target_sum = 9
result = is_subset_sum(nums, target_sum)
if result:
    print("Subset with sum {} exists.".format(target_sum))
else:
    print("No subset with sum {} exists.".format(target_sum))
