'''
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. 
words[i] + words[j] is a palindrome.
Example 1:
Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:
Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
'''
def palindromePairs(words):
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """
    l=len(words)
    if l==1:return []
    dicts={chr(i):0 for i in range(97,123)}
    nums=[0]*l
    for i in range(l):
        val=dicts.copy()
        for j in words[i]:
            val[j]+=1
        nums[i]=val
words= ["bat","tab","cat"]
palindromePairs(words)