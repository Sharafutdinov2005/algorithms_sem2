from math import inf
from typing import List
from collections import deque


class Solution:
    @staticmethod
    def findPathNum(
        adj_list: List[List[int]],
        start: int,
        end: int
    ) -> int:
        n = len(adj_list)
        distance = [inf] * n
        path_count = [0] * n

        distance[start] = 0
        path_count[start] = 1

        queue = deque([start], n)

        while queue:
            v = queue.popleft()
            for u in adj_list[v]:
                if distance[u] > distance[v] + 1:
                    distance[u] = distance[v] + 1
                    path_count[u] = path_count[v]
                    queue.append(u)
                elif distance[u] == distance[v] + 1:
                    path_count[u] += path_count[v]

        return path_count[end]


if __name__ == "__main__":
    adj_list = [
        [1, 3],
        [0, 2, 4],
        [1, 5],
        [0, 4],
        [1, 3, 5],
        [2, 4]
    ]

    print(Solution.findPathNum(adj_list, 0, 5))
