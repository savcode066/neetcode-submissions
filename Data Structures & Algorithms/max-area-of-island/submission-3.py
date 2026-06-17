class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        def bfs(r,c):
            q = collections.deque()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            area = 1

            q.append((r,c))
            visited.add((r,c))
            
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr >= 0 and nr<rows and nc>=0 and nc<cols and grid[nr][nc] == 1 and (nr, nc) not in visited):
                        q.append((nr,nc))
                        visited.add((nr,nc))
                        area += 1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    curr_area = bfs(r,c)
                    max_area = max(max_area, curr_area)
        return max_area

                    