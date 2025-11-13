from math import inf
from typing import Callable, Dict, List
from collections import deque


# inline std::vector<int> bfs_way(
#         const std::vector<std::vector<int>> &g,
#         int v0,
#         int v1)
# {
#     std::vector<int> dist(g.size(),-1);//dist
#     std::vector<int> parents(g.size(),-1);//parents
#     std::queue<int> q;
#     dist[v0] = 0;
#     q.push(v0);
#     while(!q.empty())
#     {
#         int v = q.front();
#         q.pop();
#         if(v == v1)
#             return way_from_tree(parents,v0,v1);
#         for(int u : g[v])
#         {
#             if(dist[u] == -1)
#             {
#                 dist[u] = dist[v] + 1;
#                 parents[u] = v;
#                 q.push(u);
#             }
#         }
#     }
#     return {};
# }

def way_from_tree(
    parents: Dict[int, int],
    v0: int,
    v1: int
) -> List[int]:
    way = []
    while parents.get(v0):
        v0 = parents[v0]
        way.append(v0)
    return way[::-1]


def bfs_way_infinite(
    g: Callable,
    v0: int,
    v1: int,
    dist_limit: int = 100000
) -> List:
    parent = dict()
    dist = dict()
    dist[v0] = 1
    queue = deque([v0])

    while queue:
        v = queue.popleft()
        if v == v1:
            return way_from_tree(parent, v1, v0)
        for u in g(v):
            if dist.get(u, inf) > dist[v]:
                dist[u] = dist[v] + 1
                parent[u] = v
    return []
