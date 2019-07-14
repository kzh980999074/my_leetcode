'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
Example:
Input: 
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Output: 4
'''
def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    l=len(matrix)
    if l<1:return 0
    w=len(matrix[0])
    if w<1:return 0
    for i in range(l):
        for j in range(w):
            matrix[i][j]=int(matrix[i][j])
    maxs=0
    for i in range(l):
        if matrix[i][0]==1:
            maxs=1
            break
    for i in range(w):
        if matrix[0][i]==1:
            maxs=1
            break
    for i in range(1,l):
        for j in range(1,w):
            if matrix[i][j]==1:
                diag=matrix[i-1][j-1]
                left=matrix[i][j-1]
                up=matrix[i-1][j]
                mins=min(diag,left,up)
                if mins!=0:
                    matrix[i][j]=mins+1
                    maxs=max(mins+1,maxs)
    return maxs*maxs