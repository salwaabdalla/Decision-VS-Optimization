# Optimization Subset Sum Problem
# Returns the largest subset sum ≤ target

def closest_subset_sum(S, target):
    n = len(S)
    dp = [False] * (target + 1)
    dp[0] = True

    for num in S:
        for j in range(target, num - 1, -1):
            if dp[j - num]:
                dp[j] = True

    for i in range(target, -1, -1):
        if dp[i]:
            return i
    return 0

# Example usage
if __name__ == "__main__":
    S = [3, 34, 4, 12, 5, 2]
    target = 30
    result = closest_subset_sum(S, target)
    print("Closest subset sum to", target, "is:", result)
