'''
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Input:
[[1,3,1],
  [1,5,1],
  [4,2,1]]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

def minPathSum(grid):
    if not grid:return 0
    if len(grid[0])==1:return sum([i[0] for i in grid])
    if len(grid)==1:return sum(grid[0])
    length=len(grid[0])
    width=len(grid)
    for i in range(1,len(grid)):
        grid[i][0]+=grid[i-1]
    for i in range( 1,len(grid[0]) ):
        grid[0][i]+=grid[0][i-1]

    for i in range(1,length):
        for j in range(1,width):
            grid[j][i]=min( grid[j-1]+grid[j][i], grid[j][i-1]+grid[j][i] )
    
    return grid[-1][-1]
