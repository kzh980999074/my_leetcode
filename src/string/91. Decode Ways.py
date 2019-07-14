'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
'''

def partition(s):
    length=len(s)
    l=['']*length
    k=0
    j=0
    i=0
    stat=True
    while i<length:
        if stat:
            if s[i]=='1' or s[i]=='2':
                stat=False
                j=i;i+=1
            else:
                l[k]+=s[i]
        else:
            if s[i]=='1' or s[i]=='2':
                i+=1
            elif s[i]=='0':
                l[k]+=s[j:i-1]
                i+=1;k+=1;stat=True
            
            elif s[i-1]=='1' or (s[i-1]=='2' and int(s[i])<7):
                l[k]+=s[j:i+1]
                i+=1;k+=1;stat=True
            else:
                l[k]+=s[j:i]
                i+=1;k+=1;stat=True
    if not stat:
        l[k]+=s[j:i+1]
           
    print(l)     
    return l
def fibone(n):
    l=[1]*(n+1)
    if n<2:
        return l
    else:
        for i in range(2,n+1):
            l[i]=l[i-1]+l[i-2]
    print(l)
    return l
s='121'
ss=partition(s)
ml=1
for i in ss:
    ml=max(len(i),ml)
    
L=fibone(ml)
for i in range(len(ss)):
    ss[i]=L[len(ss[i])]
print(ss)
result=1
for j in ss:
    result*=j
print(result)

    
    
    
    
    
    
                    
                
            