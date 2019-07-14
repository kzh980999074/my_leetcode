'''
Given a positive integer n, generate a square matrix filled with elements 
from 1 to n2 in spiral order.
Example:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''
def subgenerate(l,r,n,mat):
    for i in range(l,r):
        mat[l][i]=n
        n+=1
    for i in range(l+1,r):
        mat[i][r-1]=n
        n+=1
    for i in range(r-2,l-1,-1):
        mat[r-1][i]=n
        n+=1
    for i in range(r-2,l,-1):
        mat[i][l]=n
        n+=1
    return n
def generateMatrix(n):
    result=[[0]*n for i in range(n)]
    if n==1:
        return [1]
    else:
        l=0;r=n
        val=1
        while l<r:
            val=subgenerate(l,r,val,result)
            l+=1
            r-=1
    print(result)
    
generateMatrix(6)
    