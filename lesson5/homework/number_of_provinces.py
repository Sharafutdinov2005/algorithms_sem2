from typing import List


class Solution:
    @staticmethod
    def findCircleNum(
        isConnected: List[List[int]]
    ) -> int:
        n = len(isConnected)
        visited = [False] * n
        components = 0

        def dfs(v):
            visited[v] = True
            for u in range(n):
                if isConnected[v][u] and not visited[u]:
                    dfs(u)

        for v in range(n):
            if not visited[v]:
                components += 1
                dfs(v)

        return components


if __name__ == "__main__":
    m = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]

    s = Solution()
    print("result", s.findCircleNum(m))
