def count_ways(coins, n, target_sum):
    # Initialize a table to store the number of ways for each subproblem
    dp = [0] * (target_sum + 1)

    # There is one way to make sum 0, i.e., by not selecting any coin
    dp[0] = 1

    # Iterate over all coins and update the table
    for coin in coins:
        for i in range(coin, target_sum + 1):
            dp[i] += dp[i - coin]

    # The final result is stored in dp[target_sum]
    return dp[target_sum]

# Example usage:
coins = [1, 2, 5]
target_sum = 5
result = count_ways(coins, len(coins), target_sum)
print("Number of ways to make sum {}: {}".format(target_sum, result))
