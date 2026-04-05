def fibonacci(n):
    dp = [0,1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

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
    """Matrix Chain Multiplication - O(n^3)
    dimensions: list of integers where matrix i has dimensions dimensions[i-1] x dimensions[i]
    """
    n = len(dimensions) - 1
    # dp[i][j] = minimum cost to multiply matrices from i to j
    dp = [[float('inf')] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]
    
    # Base case: single matrices have 0 cost
    for i in range(n):
        dp[i][i] = 0
    
    # l is the chain length
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                # Cost of multiplying matrices i..k and k+1..j
                # Plus cost of multiplying the two result matrices
                cost = dp[i][k] + dp[k+1][j] + dimensions[i] * dimensions[k+1] * dimensions[j+1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k
    
    # Return integer minimum cost
    min_cost = int(dp[0][n-1]) if dp[0][n-1] != float('inf') else 0
    return min_cost, split

def tsp_dp(dist_matrix):
    """Travelling Salesman Problem using Dynamic Programming - O(n^2 * 2^n)
    dist_matrix: symmetric distance matrix
    """
    n = len(dist_matrix)
    if n <= 1:
        return 0, [0]
    
    # dp[mask][i] = minimum cost to visit all cities in mask ending at city i
    dp = [[float('inf')] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]
    
    # Start from city 0
    dp[1][0] = 0
    
    for mask in range(1, 1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            if dp[mask][u] == float('inf'):
                continue
            
            for v in range(n):
                if mask & (1 << v):
                    continue
                new_mask = mask | (1 << v)
                cost = dp[mask][u] + dist_matrix[u][v]
                if cost < dp[new_mask][v]:
                    dp[new_mask][v] = cost
                    parent[new_mask][v] = u
    
    # Find minimum cost to return to city 0
    full_mask = (1 << n) - 1
    min_cost = float('inf')
    last_city = -1
    
    for i in range(1, n):
        cost = dp[full_mask][i] + dist_matrix[i][0]
        if cost < min_cost:
            min_cost = cost
            last_city = i
    
    # Reconstruct path
    path = [0]
    mask = full_mask
    current = last_city
    
    while current != 0:
        path.append(current)
        prev = parent[mask][current]
        mask ^= (1 << current)
        current = prev
    
    path.reverse()
    return int(min_cost), path