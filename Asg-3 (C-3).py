'''---------------------------------------------------------------------------------------------------------------------------------------------
Problem Statement :Given two strings s1 and s2 (all letters in uppercase). Check if it is possible to convert s1 to s2 by
 performing following operations.
1. Make some lowercase letters uppercase.
2. Delete all the lowercase letters.
---------------------------------------------------------------------------------------------------------------------------------------------'''

def can_convert(s1, s2):
    m, n = len(s1), len(s2)

    dp = [[False] * (n + 1) for _ in range(m + 1)]

    dp[0][0] = True

    for i in range(1, m + 1):
        for j in range(n + 1):
            if s1[i - 1].islower():
                dp[i][j] = dp[i - 1][j]

            if j > 0 and s1[i - 1].upper() == s2[j - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - 1]

    return dp[m][n]

s1 = input("Enter the first string in uppercase: ")
s2 = input("Enter the second string in uppercase: ")

if can_convert(s1, s2):
    print(f"It is possible to convert '{s1}' to '{s2}'.")
else:
    print(f"It is not possible to convert '{s1}' to '{s2}'.")
