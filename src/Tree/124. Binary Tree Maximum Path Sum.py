import sys
class Solution:
    res = -sys.maxsize
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.helper(root)
        return self.res
    
    def helper(self, root):
        if root == None:
            return 0
        leftMax = self.helper(root.left)
        rightMax = self.helper(root.right)
        tempPath = root.val + leftMax + rightMax
        sum = root.val + max(leftMax, rightMax, 0)
        self.res = max(sum, tempPath, self.res)
        print(sum)
        return sum
[5,4,8,11,null,13,4,7,2,null,null,null,1]