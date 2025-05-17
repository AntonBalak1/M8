import heapq


def prim(graph, start):
    visited = set()
    min_heap = [(0, start, -1)]  # (weight, to, from)
    mst = []
    total_cost = 0

    while min_heap:
        weight, node, prev = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            if prev != -1:
                mst.append((prev, node, weight))
                total_cost += weight
            for neighbor, w in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (w, neighbor, node))

    return mst, total_cost



class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        self.parent[pu] = pv
        return True

def kruskal(edges, num_nodes):
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(num_nodes)
    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost



graph = {
    0: [(1, 4), (2, 1)],
    1: [(0, 4), (2, 2), (3, 5)],
    2: [(0, 1), (1, 2), (3, 8)],
    3: [(1, 5), (2, 8)]
}

edges = [
    (0, 1, 4),
    (0, 2, 1),
    (1, 2, 2),
    (1, 3, 5),
    (2, 3, 8)
]

prim_mst, prim_cost = prim(graph, 0)
kruskal_mst, kruskal_cost = kruskal(edges, 4)

print("Prim's MST:", prim_mst)
print("Prim's Total Cost:", prim_cost)

print("Kruskal's MST:", kruskal_mst)
print("Kruskal's Total Cost:", kruskal_cost)
