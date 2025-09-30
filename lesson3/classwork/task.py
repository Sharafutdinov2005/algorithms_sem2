def topological_sort(graph: list[list[int]]):
    visited = [False] * len(graph)
    sorted_list = []

    def dfs(v: int):
        visited[v] = True
        for u in graph[v]:
            if not visited[u]:
                dfs(u)
        sorted_list.append(v)

    for v in range(len(graph)):
        if not visited[v]:
            dfs(v)

    return sorted_list[::-1]


names = [
    "Трусы",
    "Носки",
    "Брюки",
    "Туфли",
    "Ремень",
    "Рубашка",
    "Галстук",
    "Пиджак",
    "Часы"
]

graph = [
    [2, 3],
    [3],
    [4, 5],
    [],
    [7],
    [4, 6],
    [7],
    [],
    []
]

for i in topological_sort(graph):
    print(names[i])
