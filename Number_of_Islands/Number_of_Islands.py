class Solution:
    '''def dfs(self,grid,i,j):
        if(i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=='0'):
            return
        grid[i][j]='0'
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j-1)
        self.dfs(grid,i,j+1)        
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands=0
        m=len(grid)
        if m==0: return 0 
        n=len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    print(i,j)
                    self.dfs(grid,i,j)
                    islands+=1
        return islands'''
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        q = collections.deque()
       
        island=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    q.append((i,j))
                    self.bfs(q,grid)
                    island+=1
        #print(q)
        return island
        
    def bfs(self,q,grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy                                
                if 0<=nx<m and 0<=ny<n and grid[nx][ny] !='0': 
                    grid[nx][ny] = '0'
                    q.append((nx,ny))
                    #print('-----------',q)
        
            
            
            
            
        