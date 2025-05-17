from collections import defaultdict, deque

class SocialNetwork:
    def __init__(self):
        self.graph = defaultdict(set)

    def add_user(self, name):
        self.graph[name]  # creates entry if not exists

    def add_friendship(self, user1, user2):
        self.graph[user1].add(user2)
        self.graph[user2].add(user1)

    def are_connected(self, user1, user2):
        visited = set()
        queue = deque([user1])

        while queue:
            current = queue.popleft()
            if current == user2:
                return True
            visited.add(current)
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return False

    def list_friends(self, user):
        return list(self.graph[user])

    def largest_group(self):
        visited = set()
        max_group = []

        def bfs(start):
            queue = deque([start])
            group = []
            while queue:
                node = queue.popleft()
                if node not in visited:
                    visited.add(node)
                    group.append(node)
                    for neighbor in self.graph[node]:
                        if neighbor not in visited:
                            queue.append(neighbor)
            return group

        for user in self.graph:
            if user not in visited:
                group = bfs(user)
                if len(group) > len(max_group):
                    max_group = group
        return max_group



net = SocialNetwork()
users = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
for u in users:
    net.add_user(u)

net.add_friendship("Alice", "Bob")
net.add_friendship("Bob", "Charlie")
net.add_friendship("David", "Eve")

print("Is Alice connected to Charlie?", net.are_connected("Alice", "Charlie"))
print("Is Alice connected to Eve?", net.are_connected("Alice", "Eve"))
print("Friends of Bob:", net.list_friends("Bob"))
print("Largest group:", net.largest_group())
