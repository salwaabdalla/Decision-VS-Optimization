# Decision Subset Sum Problem
# Returns True if there is a subset of the given list that adds up to the target sum

def is_subset_sum(S, target):
    n = len(S)
    # Initialize DP table
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # Base case: sum 0 is always possible with empty set
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if S[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - S[i - 1]]

    return dp[n][target]

# Example usage
if __name__ == "__main__":
    S = [3, 34, 4, 12, 5, 2]
    target = 9
    result = is_subset_sum(S, target)
    print("Subset sum possible:", result)
