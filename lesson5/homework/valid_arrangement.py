from typing import List, Dict, Tuple


class Solution:
    @staticmethod
    def _find_semieil_start(
        ins,
        outs,
    ) -> int:
        for v in outs:
            start = v
            if outs[v] > ins.get(v, -1):
                break
        return start  # in full eiler graph exists cycle

    def _build_adjacency_list_with_begining(
        self,
        edges: List[List[int]]
    ) -> Tuple[Dict[int, List[int]], int]:
        graph = {}
        ins = {}
        outs = {}

        for u, v in edges:

            if graph.get(u) is None:
                graph[u] = []
            if v not in graph:
                graph[v] = []

            graph[u].append(v)
            outs[u] = outs.get(u, 0) + 1
            ins[v] = ins.get(v, 0) + 1

        return graph, self._find_semieil_start(ins, outs)

    @staticmethod
    def _find_eilr_path(
        graph: Dict[int, List[int]],
        start: int
    ) -> List[int]:
        result_path = []

        def dfs(v):
            while graph.get(v) and graph[v]:
                u = graph[v].pop(0)
                dfs(u)
                result_path.append([v, u])

        dfs(start)

        return result_path[::-1]

    def validArrangement(
        self,
        pairs: List[List[int]]
    ) -> List[List[int]]:
        graph, start = self._build_adjacency_list_with_begining(pairs)
        return self._find_eilr_path(graph, start)


if __name__ == "__main__":
    p = [
        [5, 1],
        [4, 5],
        [11, 9],
        [9, 4]
    ]
    s = Solution()
    print(s.validArrangement(p))
