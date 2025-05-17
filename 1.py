from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def dfs(self, start):
        visited = set()
        order = []

        def dfs_recursive(node):
            visited.add(node)
            order.append(node)
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return order

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        order = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                order.append(node)
                for neighbor in self.adj_list[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return order


graph = Graph()
edges = [
    ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'),
    ('D', 'E'), ('E', 'F')
]

for u, v in edges:
    graph.add_edge(u, v)

start_node = 'A'
print("DFS Order:", graph.dfs(start_node))
print("BFS Order:", graph.bfs(start_node))
