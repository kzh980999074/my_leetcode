'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
'''

def isInterleave(s1,s2,s3):
    def dfs(i, j, k):
        if (i, j, k) not in memo:
            memo[(i, j, k)] = k>=l3 or (i<l1 and s3[k]==s1[i] and dfs(i+1,j,k+1)) or (j<l2 and s3[k]==s2[j] and dfs(i,j+1,k+1))
        print(memo)
        return memo[(i, j, k)]
    l1, l2, l3, memo = len(s1), len(s2), len(s3), {}
    if l3 != l1 + l2: return False
    return dfs(0, 0, 0)
print(isInterleave('a','b','ab'))