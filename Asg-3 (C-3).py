def can_convert(s1, s2):
    m, n = len(s1), len(s2)

    # Create a 2D table to store the results of subproblems
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # An empty string can always be converted to another empty string
    dp[0][0] = True

    # Fill the table using bottom-up dynamic programming
    for i in range(1, m + 1):
        for j in range(n + 1):
            # Case 1: If characters match, result depends on previous subproblem
            if j > 0 and s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # Case 2: Uppercase current character in s1
            elif s1[i - 1].islower():
                dp[i][j] = dp[i - 1][j]
            # Case 3: Delete lowercase character in s1
            elif j > 0 and s1[i - 1].isupper():
                dp[i][j] = dp[i - 1][j]

    # The final result is stored in dp[m][n]
    return dp[m][n]

# Example usage:
s1 = "ABcd"
s2 = "ABC"
result = can_convert(s1, s2)

if result:
    print("It is possible to convert {} to {}.".format(s1, s2))
else:
    print("It is not possible to convert {} to {}.".format(s1, s2))
