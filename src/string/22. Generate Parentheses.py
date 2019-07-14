'''
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"]
'''
def generateParenthesis(n):
    result=set([''])
    while n>0:
        newset=set()
        for i in result:
            newset.add('('+i+')')
            for j in range(len(i)):
                newset.add(i[:j]+'()'+i[j:])
        result=newset
        n-=1
    print(result)
    print(len(result))
generateParenthesis(10)