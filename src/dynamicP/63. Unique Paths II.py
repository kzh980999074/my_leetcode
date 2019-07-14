'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
 The robot is trying to reach the bottom-right corner of the grid 
 (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

'''
obstacle=[[0,0,0],
          [0,1,0],
          [0,0,0]]

def uniquePath(obstacleGrid):
    length=len(obstacleGrid[0])
    width=len(obstacleGrid)
    j=0
    
    for i in range(length):
        if  obstacleGrid[0][i]==0:
            obstacleGrid[0][i]=1
        else:
            j=i
            break
    if j!=0:
        
        for i in range(j,length):
            obstacleGrid[0][i]=0
    
    j=0
    for i in range(1,width):
        if obstacleGrid[i][0]==0:
            obstacleGrid[i][0]=1
        else:
            j=i
            break
    if j!=0:
        for i in range(j,width):
            obstacleGrid[i][0]=0
      
      
    for i in range(1,width):
        for j in range(1,length):
            if obstacleGrid[i][j]!=1:
                obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
            else:
                obstacleGrid[i][j]=0
    return obstacleGrid[-1][-1]
uniquePath(obstacle)

