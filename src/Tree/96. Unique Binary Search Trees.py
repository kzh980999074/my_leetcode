'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
Example:
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

def numsTree(n):
    if n==0:return 1
    if n==1:return 1
    if n==2:return 2
    if n==3:return 5
    mat=[0]*(n+1)
    mat[:4]=[1,1,2,5]
    for i in range(4,n+1):
        val=0
        for j in range(i):
            val+=mat[j]*mat[i-j-1]
        mat[i]=val
    return mat[-1]
print(numsTree(66))
        