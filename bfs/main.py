class Node:
    def __init__(self, name):
        self.name = name
        self.references = []


from collections import deque


def bfs_reachable_nodes(root_nodes):
    reachable = set()
    queue = deque(root_nodes)

    while queue:
        node = queue.popleft()
        if node in reachable:
            continue
        reachable.add(node)
        for ref in node.references:
            queue.append(ref)
    return reachable


def find_leak_nodes(all_nodes, root_nodes):
    reachable = bfs_reachable_nodes(root_nodes)
    return [node for node in all_nodes if node not in reachable]


# Test
a = Node("Activity")
b = Node("View")
c = Node("Listener")
d = Node("Bitmap")
e = Node("LeakedObject")

a.references = [b, c]
b.references = [d]
e.references = []  # e is not referenced

all_nodes = [a, b, c, d, e]
gc_roots = [a]  # Activity as GC Root

leaks = find_leak_nodes(all_nodes, gc_roots)
print("Leaked Nodes (unreachable from GC roots):")
for node in leaks:
    print(node.name)
