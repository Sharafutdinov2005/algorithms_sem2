def find_bridges():
    pass


def find_undir_components():
    pass


def find_bi_edge_components(
    graph: list[list[int]],
) -> list[list[int]]:
    bridges = set(find_bridges())

    # inline std::vector< int > undir_components(const std::vector<std::vector<int>> &g)
    # {
    #     std::vector<bool> visited(g.size());
    #     std::vector<int> components(g.size());
    #     int ci = 0;
    #     std::function<void(int)> dfs = [&](int v)
    #     {
    #         visited[v] = true;
    #         components[v] = ci;
    #         for(int u : g[v])
    #             if(visited[u] == false)
    #                 dfs(u);
    #     };
    #     for(int v = 0; v < g.size() ; ++v)
    #     {
    #         if(visited[v] == false)
    #         {
    #             dfs(v);
    #             ++ci;
    #         }
    #     }
    #     return components;
    # }

    visited = [False] * len(graph)
    components = [0] * len(graph)
    ci = 0

    def DFS(v):
        visited[v] = True
        components[v] = ci
        for u in graph[v]:
            if (u, v) in bridges or (v, u) in bridges:
                continue
            elif not visited[u]:
                DFS(u)

    for v in range(len(graph)):
        if not visited[v]:
            DFS(v)

    return components
