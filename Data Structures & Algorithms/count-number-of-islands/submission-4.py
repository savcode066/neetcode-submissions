class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        row = len(grid)
        col = len(grid[0])
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                node = q.popleft()
                visited.add(node)
                curr_r = node[0]
                curr_c = node[1]

                directions = [[0,1],[1,0],[-1,0],[0,-1]]
                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc
                    if nr >= 0 and nr < row and nc >= 0 and nc < col and grid[nr][nc]!="0" and (nr, nc) not in visited:
                        q.append((nr,nc))
                        
            
                
        
        num_islands = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    num_islands += 1
        return num_islands

        
        