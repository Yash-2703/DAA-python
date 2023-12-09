'''---------------------------------------------------------------------------------------------------------------------------------------------
Problem Statement :Given an integer array of coins[ ] of size N representing different types of currency and an
integer sum, The task is to find the number of ways to make sum by using different combinations from coins[].
---------------------------------------------------------------------------------------------------------------------------------------------'''

def count_ways(coins, n, target_sum):
    dp = [0] * (target_sum + 1)

    dp[0] = 1

    for coin in coins:
        for i in range(coin, target_sum + 1):
            dp[i] += dp[i - coin]

    return dp[target_sum]

coins = [1, 2, 5]
target_sum = 5
result = count_ways(coins, len(coins), target_sum)
print("Number of ways to make sum {}: {}".format(target_sum, result))
