'''Given an array of strings, group anagrams together.
Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''
def groupAngrams(strs):
    dicts={}
    for s in strs:
        ones=list(s)
        l=list(s)
        l.sort()
        s1=''.join(l)
        dicts.setdefault(s1,[])
        dicts[s1].append(s)
    result=list(dicts.values())
    return result
