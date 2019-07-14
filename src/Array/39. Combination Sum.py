'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
 find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.
Note:
    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[[2,2,2,2],
  [2,3,3],
  [3,5]]
'''
sums=[]
def combinationSum(canditates,target,result=[],start=0):
    l=len(canditates)
    for i in range(start,l):
        val=target-canditates[i]
        if val>=0:
            cr=result.copy()
            cr.append(canditates[i])
            if val==0:
                sums.append(cr)
            else:
                combinationSum(canditates,val,cr,i)
        else:
            break
combinationSum([2,3,5,7],7)
print(sums)