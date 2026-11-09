class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        fresh = 0

        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    visited.add((row, col))
                    q.append((row, col))

        time = 0

        while q and fresh:
            size = len(q)
            dimensions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for i in range(size):
                r, c = q.popleft()
                for dr, dc in dimensions:
                    row, col = r + dr, c + dc
                    if (
                        row in range(rows)
                        and col in range(cols)
                        and grid[row][col] == 1
                        and (row, col) not in visited
                    ):
                        q.append((row, col))
                        visited.add((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
