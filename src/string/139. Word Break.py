'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words.
Note:
    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.
Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def helper(s,subs):
            result=[]
            l=len(subs)
            ls=len(s)
            for i in range(l,ls+1):
                if s[i-l:i]==subs:
                    result.append([i-l,i])
            return result
        l=len(s)
        T=[set() for _ in range(l)]
        for word in wordDict:
            arrs=helper(s,word)
            for arr in arrs:
                T[arr[0]].add(arr[1])
        stack=set()
        for i in T[0]:
            stack.add(i)
            if i ==l:return True
        while stack:
            p=stack.pop()
            for i in T[p]:
                if i==l:return True
                stack.add(i)
        return False