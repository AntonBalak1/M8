from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def has_cycle(self):
        visited = set()
        parent = {}

        def dfs(node, prev):
            visited.add(node)
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    parent[neighbor] = node
                    if dfs(neighbor, node):
                        return True
                elif neighbor != prev:
                    # Found a back edge (cycle)
                    print("Cycle detected:")
                    self.print_cycle(node, neighbor, parent)
                    return True
            return False

        for node in self.adj_list:
            if node not in visited:
                parent[node] = None
                if dfs(node, None):
                    return True
        print("No cycles.")
        return False

    def print_cycle(self, start, end, parent):
        path = [start]
        while start != end:
            start = parent[start]
            path.append(start)
        path.reverse()
        path.append(path[0])  # close the cycle
        print(" -> ".join(map(str, path)))


graph = Graph()
edges = [
    (1, 2), (2, 3), (3, 4), (4, 2),  # cycle: 2-3-4-2
    (5, 6)
]

for u, v in edges:
    graph.add_edge(u, v)

graph.has_cycle()
