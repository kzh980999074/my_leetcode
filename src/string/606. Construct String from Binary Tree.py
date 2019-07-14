'''
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     
Output: "1(2(4))(3)"
Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 
Output: "1(2()(4))(3)"
'''

def tree2str(t):
    """
    :type t: TreeNode
    :rtype: str
    """
    if not t:return ""
    if t.right==None and t.left==None:
        return str(t.val)
    if t.right!=None and t.left!=None:
        return str(t.val)+'('+self.tree2str(t.left)+')'+'('+self.tree2str(t.right)+')'
    if t.left != None:
        return str(t.val)+'('+self.tree2str(t.left)+')'
    return str(t.val)+'()'+'('+self.tree2str(t.right)+')'