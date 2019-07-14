'''
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
def subsets(nums):
    l=len(nums)
    if l==0:
        return [[]]
    elif l==1:
        return [[],nums]
    res=subsets(nums[1:])
    for i in range(len(res)):
        res.append([nums[0]]+res[i])
    return res





nums=[i for i in range(2)]
print(subsets(nums))