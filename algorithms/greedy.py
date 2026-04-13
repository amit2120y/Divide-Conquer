def fractional_knapsack(weights, values, capacity):
   
    n = len(values)
    ratio = []
    for i in range(n):
        ratio.append((values[i] / weights[i], weights[i], values[i]))

   
    ratio.sort(key=lambda x: x[0], reverse=True)

    total_profit = 0.0
    
   
    for r, w, p in ratio:
        if capacity >= w:
            
            capacity -= w
            total_profit += p
        else:
           
            total_profit += p * (capacity / w)
            break  
            
    return total_profit

def kruskal_algorithm(n, edges):
    class UnionFind:
        """Data structure to efficiently detect cycles (connected components)"""
        def __init__(self, n):
            self.parent = list(range(n)) 
            self.rank = [0] * n 
        
        def find(self, x):
            """Find the root/representative of vertex x's component"""
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])  
            return self.parent[x]
        
        def union(self, x, y):
           
            root_x = self.find(x)
            root_y = self.find(y)
            
            
            if root_x == root_y:
                return False
            
            
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            
            return True
    
   
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
    import heapq
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    visited = [False] * n
    mst = []
    total_weight = 0
    heap = [(0, 0, -1)]
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