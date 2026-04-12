def fractional_knapsack(weights, values, capacity):
    # 1. Calculate Profit-Weight Ratio for each item
    n = len(values)
    ratio = []
    for i in range(n):
        ratio.append((values[i] / weights[i], weights[i], values[i]))

    # 2. Sort items in descending order based on the ratio
    # x[0] refers to the ratio (profit/weight)
    ratio.sort(key=lambda x: x[0], reverse=True)

    total_profit = 0.0
    
    # 3. Iterate through sorted items to fill the knapsack
    for r, w, p in ratio:
        if capacity >= w:
            # Add the whole item if capacity allows
            capacity -= w
            total_profit += p
        else:
            # Add a fraction of the item if capacity is limited
            total_profit += p * (capacity / w)
            break  # Knapsack is full
            
    return total_profit

def kruskal_algorithm(n, edges):
    """Kruskal's Algorithm for Minimum Spanning Tree - O(E log E)"""
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n
        
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def union(self, x, y):
            px, py = self.find(x), self.find(y)
            if px == py:
                return False
            if self.rank[px] < self.rank[py]:
                px, py = py, px
            self.parent[py] = px
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1
            return True
    
    # edges format: [(u, v, weight), ...]
    edges_sorted = sorted(edges, key=lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    total_weight = 0
    
    for u, v, w in edges_sorted:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_weight += w
            if len(mst) == n - 1:
                break
    
    return mst, total_weight

def prim_algorithm(n, edges):
    """Prim's Algorithm for Minimum Spanning Tree - O(E log V)"""
    import heapq
    
    # Build adjacency list
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    visited = [False] * n
    mst = []
    total_weight = 0
    heap = [(0, 0, -1)]  # (weight, node, parent)
    
    while heap:
        w, u, parent = heapq.heappop(heap)
        
        if visited[u]:
            continue
        
        visited[u] = True
        if parent != -1:
            mst.append((parent, u, w))
            total_weight += w
        
        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(heap, (weight, v, u))
    
    return mst, total_weight

def optimal_merge_pattern(file_sizes):
    """Optimal Merge Pattern - O(n log n)"""
    import heapq
    
    if not file_sizes:
        return 0
    
    heap = file_sizes[:]
    heapq.heapify(heap)
    total_cost = 0
    merges = []
    
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        merged = first + second
        total_cost += merged
        merges.append((first, second, merged))
        heapq.heappush(heap, merged)
    
    return total_cost, merges