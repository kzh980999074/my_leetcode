'''
Given an array where elements are sorted in ascending order, 
convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in 
which the depth of the two subtrees of every node never differ by more than 1.
Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.right=None
        self.left=None
def sortedArrayToBST(nums):
    node=None
    if len(nums)>0:
        node=TreeNode(0)
        node.value=nums[len(nums)//2]
        node.left=sortedArrayToBST(nums[:len(nums)//2])
        node.right=sortedArrayToBST(nums[len(nums)//2+1:])
    return node

