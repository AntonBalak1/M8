from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def connected_components(self):
        visited = set()
        components = []

        def dfs(node, component):
            visited.add(node)
            component.append(node)
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        for node in self.adj_list:
            if node not in visited:
                component = []
                dfs(node, component)
                components.append(component)

        return components


graph = Graph()
edges = [
    (1, 2), (2, 3), (4, 5), (6, 7), (7, 8)
]

for u, v in edges:
    graph.add_edge(u, v)

components = graph.connected_components()

print(f"Total connected components: {len(components)}")
for i, comp in enumerate(components, 1):
    print(f"Component {i}: Nodes = {comp}, Size = {len(comp)}")
