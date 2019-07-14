'''
Given a string S and a string T, find the minimum window in S which will contain 
all the characters in T in complexity O(n).Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
'''
#未完成
from collections import deque
def minWindow(s,t):
    d={}
    count={}
    ls=len(s)
    lt=len(t)
    for i in t:  #计数
        count.setdefault(i,0)
        count[i]+=1
    
    address=deque()
    for i in range(ls):
        if count.get(s[i],0)!=0:
            address.append(i)
    cc={}
    end=0
    
    for i in range(len(address)):
        cc.setdefault(s[address[i] ],0)
        cc[ s[ address[i] ] ]+=1
        if cc[s[address[i]]]<=count[s[address[i]]]:
            lt-=1
        if lt<=0:
            end=i
            break
        
    if lt>0:return ''
    start=0
    for i in range(len(address)):
        if cc[s[address[i]]]>count[s[address[i]]]:
            start+=1
            cc[s[address[i]]]-=1
        else:
            break
    ll=address[end]-address[start]
    la=len(address)
    end+=1
    while end<la:
        cc[s[address[end]]]+=1
        while cc[s[address[start]]]-1>=count[s[address[start]]]:
            cc[s[address[start]]]-=1
            start+=1
        val=address[end]-address[start]
        ll=min(ll,val)
        end+=1
    print(ll)
    return ll
        
    
s='ABDDSCABNCXSAAX'
p='ABC'
minWindow(s, p)

    
        
            
    
    
    
    
    
        