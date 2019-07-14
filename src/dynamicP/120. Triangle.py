
'''
Given a triangle, find the minimum path sum from top to bottom. 
Each step you may move to adjacent numbers on the row below.
For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]-
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
'''
def minimumTotal(triangle):
    length=len(triangle)
    if length<2:
        return triangle[0][0]
    else:
        for i in range(1,length):
            
            for j in range(i+1):
                if j==0:
                    triangle[i][j]+=triangle[i-1][j]
                elif j==i:
                    triangle[i][j]+=triangle[i-1][j-1]
                else:
                    triangle[i][j]+=min(triangle[i-1][j],triangle[i-1][j])
    mini=triangle[-1][0]
    for i in range(1,length):
        mini=min(mini,triangle[-1][i])
    return mini

        
        
        
