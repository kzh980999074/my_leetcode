'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
Example:
Input: n = 4, k = 2
Output:
[  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],]
'''
def combine(n,k):
    result=[]
    for i in range(n,k-1,-1):
        if k!=1:
            tmpLists=combine(i-1,k-1)
            for tmpList in tmpLists:
                result.append(tmpList+[i])
        else:
            result.append([i])

    return result
def combine1(n,k):
    result=[]
    for i in range(n,k-1,-1):
        result.append([i])
    l=k-1
    stack=[]
    while l>0:
        for i in result:
            j=i[-1]
            for k in range(j-1,l-1,-1):
                stack.append(i+[k])
        result=stack
        stack=[]
        l-=1
    return result
print(combine1(3,3))