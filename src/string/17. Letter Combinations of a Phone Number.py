'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''
dic={}
for i in range(8):
    dic[i+2]=[chr(97+i*3+j) for j in range(3)]
dic[9].append('z')
dic[1]=[]
dic[0]=[]
def letterCombinations(digits,result=[]):
    if digits==0 or digits==1:
        return result
    else:
        d=digits%10
        digits=digits//10
        if d==1 or d==0:
            return letterCombinations(digits, result)
        else:
            if not result:
                result=[0]*len(dic[d])
                result=[i for i in dic[d]]
                return letterCombinations(digits, result)
            else:
                l=len(dic[d])
                l1=len(result)
                newresult=[0]*(len(result)*l)
                for i in range(l):
                    for j in range(l1):
                        newresult[i*l1+j]=dic[d][i]+result[j]
                return letterCombinations(digits, newresult)
print(letterCombinations(235))         