'''
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
Example:
Input: "aab"
Output:
[["aa","b"],
  ["a","a","b"]]
'''

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_palindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
            
        ans = [[] for _ in range(len(s)+1)]
        ans[0].append([])
        for i in range(len(s)):
            for start in range(i+1):
                if is_palindrome(s, start, i):
                    substr = s[start:i+1]
                    for parts in ans[start]:
                        ans[i+1].append(parts + [substr])
        print(ans)
        return ans[-1]