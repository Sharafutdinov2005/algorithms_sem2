from enum import Enum


class Color(Enum):
    """
    Enum class for marking graph nods.
    """
    White = 0
    Gray = 1
    Black = 3


def undir_has_cycle(graph):
    visited = [0] * len(graph)

    def DFS(node, node_parent):
        visited[node] = 1
        for u in graph[node]:
            if u != node_parent and (visited[u] or DFS(u, node)):
                return True
        return False

    for node in range(len(graph)):
        if not visited[node] and DFS(node, -1):
            return True

    return False


def check_path(graph, start, end):
    visited = [0] * len(graph)

    def DFS(node):
        visited[node] = 1
        for u in graph[node]:
            if not visited[u] and (u == end or DFS(u)):
                return True
        return False

    return DFS(start)


def find_path(graph, start, end):
    visited = [0] * len(graph)

    def DFS(node):
        visited[node] = 1
        for u in graph[node]:
            if u == end:
                return [u]

            if not visited[u]:
                path = DFS(u)
                if path:
                    return [u] + path

    return [start] + DFS(start)
