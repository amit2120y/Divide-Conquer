def knapsack_dp(values, weights, W):
    n = len(values)
    dp = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(W+1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w],
                               values[i-1] + dp[i-1][w-weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    return dp[m][n]

def matrix_chain_multiply(dimensions):
    n = len(dimensions) - 1
    dp = [[float('inf')] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + dimensions[i] * dimensions[k+1] * dimensions[j+1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k
    min_cost = int(dp[0][n-1]) if dp[0][n-1] != float('inf') else 0
    return min_cost, split