'''
Given an integer n, generate all structurally unique BST's 
(binary search trees) that store values 1 ... n.
Example:
Input: 3
Output:
[[1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

def generateTrees(self, n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
    def dfs(l, r):
        if r < l: return [None]
        arr = []
        for m in range(l, r + 1):
            left = dfs(l, m - 1)
            right = dfs(m + 1, r)
            for lNode in left:
                for rNode in right:
                    new = TreeNode(m)
                    new.left = lNode
                    new.right = rNode
                    arr.append(new)
        return arr
    res = dfs(1, n)
    return [] if res == [None] else res