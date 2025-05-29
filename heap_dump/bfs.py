# Tree Structure:
# A
# ├── B
# │   ├── D
# │   └── E
# │       └── G
# └── C
#     └── F


class Node:
    def __init__(self, name):
        self.name = name
        self.references = []


# Create nodes
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")

# Build reference relationships (undirected graph)
a.references = [b, c]
b.references = [a, d, e]
c.references = [a, f]
d.references = [b]
e.references = [b, g]
f.references = [c]
g.references = [e]


from collections import deque


def bfs(start_node):
    pass


# Test
bfs(a)

# Expect:
# - A
# - B
# - C
# - D
# - E
# - F
# - G
