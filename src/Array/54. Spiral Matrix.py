'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
Example 1:
Input:
[[ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:
Input:
[[1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
def spiralOrder(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if not matrix:return []
    if not matrix[0]:return []
    result=[0]*(len(matrix)*len(matrix[0]))
    row=len(matrix);column=len(matrix[0])
    i=0;j=0
    k=0;s=0
    while i<row and j<column:
        if k%4==0:
            for p in range(j,column):
                result[s]=matrix[i][p]
                s+=1
            i+=1
            k+=1
        elif k%4==1:
            for p in range(i,row):
                result[s]=matrix[p][column-1]
                s+=1
            column-=1
            k+=1
        elif k%4==2:
            for p in range(column-1,j-1,-1):
                result[s]=matrix[row-1][p]
                s+=1
            row-=1
            k+=1
        else:
            for p in range(row-1,i-1,-1):
                result[s]=matrix[p][j]
                s+=1
            j+=1
            k+=1
    return result