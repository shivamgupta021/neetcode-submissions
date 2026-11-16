class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0
            if minCost[i] != -1:
                return minCost[i]

            minCost[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return minCost[i]

        return min(dfs(0), dfs(1))

            