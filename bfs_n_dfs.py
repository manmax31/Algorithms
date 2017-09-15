# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
"""
Depth First Search:
On each visit to a node:
    1. Mark the current vertex as being visited.
    2. Explore each adjacent vertex that is not included in the visited set.
"""

def dfs_loop(graph, start):
    """
    Returns connected components
    :param graph:
    :param start:
    :return:
    """
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


def dfs_recursion(graph, start, visited=None):
    """
    Returns connected components
    :param graph:
    :param start:
    :param visited:
    :return:
    """
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs_recursion(graph, next, visited)
    return visited


def dfs_paths_loop(graph, start, goal):
    """
    Returns Path
    :param graph:
    :param start:
    :param goal:
    :return:
    """
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def dfs_paths_recursion(graph, start, goal, path=None):
    """
    Returns Path
    :param graph:
    :param start:
    :param goal:
    :param path:
    :return:
    """
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths_recursion(graph, next, goal, path + [next])


def bfs_loop(graph, start):
    """
    Connected Components
    :param graph:
    :param start:
    :return:
    """
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def bfs_paths(graph, start, goal):
    """
    Paths
    :param graph:
    :param start:
    :param goal:
    :return:
    """
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):
    """
    Shortest path using BFS.
    It should be Single-Pair and Single-Source
    O(|V|+|E|)
    :param graph:
    :param start:
    :param goal:
    :return:
    """
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print(dfs_loop(graph, 'A'))       # {'E', 'D', 'F', 'A', 'C', 'B'}
print(dfs_recursion(graph, 'A'))  # {'E', 'D', 'F', 'A', 'C', 'B'}
print(bfs_loop(graph, 'A'))       # {'B', 'C', 'A', 'F', 'D', 'E'}
print(list(dfs_paths_loop(graph, 'A', 'F')))
print(list(bfs_paths(graph, 'A', 'F')))
print(shortest_path(graph, 'A', 'F'))
