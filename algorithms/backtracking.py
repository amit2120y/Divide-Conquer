def n_queens(n):
    board = [-1]*n
    solutions = []

    def is_safe(row, col):
        for i in range(row):
            if board[i] == col or abs(board[i]-col) == abs(i-row):
                return False
        return True

    def solve(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                solve(row+1)

    solve(0)
    return solutions

def tsp_dp(dist_matrix):
    n = len(dist_matrix)
    if n <= 1:
        return 0, [0]
    dp = [[float('inf')] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]
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
    full_mask = (1 << n) - 1
    min_cost = float('inf')
    last_city = -1
    for i in range(1, n):
        cost = dp[full_mask][i] + dist_matrix[i][0]
        if cost < min_cost:
            min_cost = cost
            last_city = i
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