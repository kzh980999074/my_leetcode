def reverseStr(s, k):
    l=len(s)
    if k<=1:
        return s
    elif k>=l:
        return s[::-1]
    else:
        times=l//(2*k)
        result=''
        i=0
        while i<times: 
            s1=''.join(list(reversed(s[i*2*k:2*i*k+k])))
            result+=s1+s[2*i*k+k:2*i*k+2*k]
            i+=1
            print(result)
        reminder=s[2*i*k:]
        print(result)
        if len(reminder)<=k:
            print(result)
            return result+reminder[::-1]
        else:
            return result+reminder[:k][::-1]+reminder[k:]
        
s='abcdfg'
s1=reverseStr(s,2)
print(s1)