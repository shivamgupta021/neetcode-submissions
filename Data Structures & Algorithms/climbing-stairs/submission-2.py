from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(remaining):
            if remaining < 0:
                return 0
            if remaining == 0:
                return 1

            return dfs(remaining - 1) + dfs(remaining - 2)
        
        return dfs(n)