from typing import List, Dict


class Solution:
    @staticmethod
    def _build_graph(
        tickets: List[List[str]]
    ) -> Dict[str, List[str]]:
        graph = {}
        for st, end in tickets:
            if st not in graph:
                graph[st] = []
            graph[st].append(end)
        return graph

    @staticmethod
    def _sort_graph(
        graph: Dict[str, List[str]]
    ) -> None:
        for adj in graph:
            graph[adj].sort(reverse=True)

    @staticmethod
    def _find_eilr_path(
        graph: Dict[str, List[str]],
    ) -> List[str]:
        itinerary = []

        def dfs(u: str):
            while u in graph and graph[u]:
                v = graph[u].pop()
                dfs(v)
            itinerary.append(u)

        dfs("JFK")

        return itinerary[::-1]

    def findItinerary(
        self,
        tickets: List[List[str]]
    ) -> List[str]:
        graph = self._build_graph(tickets)

        self._sort_graph(graph)

        return self._find_eilr_path(graph)


if __name__ == '__main__':
    t = [
        ["JFK", "SFO"],
        ["JFK", "ATL"],
        ["SFO", "ATL"],
        ["ATL", "JFK"],
        ["ATL", "SFO"]
    ]

    s = Solution()
    print("result:", s.findItinerary(t))
