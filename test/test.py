
def str_mul(L1,L2):
    l1=list(reversed(L1))
    l2=list(reversed(L2))
    new_l=[0]*( len(l1)+len(l2) )
    for i in range(len(l1)):
        for j in range(len(l2)):
            k=l1[i]*l2[j]
            new_l[i+j]+=k
    
    for i in range(len(l1)+len(l2)-1):
        new_l[i+1]+=new_l[i]//10
        new_l[i]=new_l[i]%10
    if new_l[-1]==0:
        del new_l[-1]
    new_l.reverse()
    
    return new_l
def str_add(L1,L2):
    l=[0]*(max(len(L2),len(L1))+1)
    len1=len(L1)
    len2=len(L2)
    l1=list(reversed(L1))
    l2=list(reversed(L2))
    for i in range(min(len1,len2)):
        l[i] +=l1[i]+l2[i]
        if l[i]>9:
            l[i+1]+=1
            l[i]=l[i]%10
    if len2>len1:
        for i in range(len1,len2):
            l[i]+=l2[i]
            if l[i]>9:
                l[i+1]+=1
                l[i]=l[i]%10
    else:
        for i in range(len2,len1):
            l[i]+=l1[i]
            if l[i]>9:
                l[i+1]+=1
                l[i]=l[i]%10
    if l[-1]==0:
        del l[-1]
    l.reverse()
    return  l
                

    
    
l1=[1]
l2=[1,2,3,4,5]
print(str_mul(l1,l2))
print(str_add(l1,l2))

def str_pow(l,n):
    if n==0:
        return [1]
    if n==1:
        return l
    elif n%2==0:
        ll=str_mul(l,l)
        return str_pow(ll,n//2)
    else :
        ll=str_mul(l,l)
        return str_mul(str_pow(ll,n//2),l )

print(str_pow(l2,3))
    
    
    
    
    
    