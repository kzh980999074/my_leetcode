'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''
def restoreIpAddresses(s):

    length=len(s)
    if length<4 or length>12:return []
    result=[]
    d0=2 if s[0]=='0' else 4
    for i in range(1,min(d0,length-2)):
        if int(s[:i])<256:
            d1=i+2 if s[i]=='0' else i+4
            for j in range(i+1,min(d1,length-1)):
                if int(s[i:j])<256:
                    d2=j+2 if s[j]=='0' else j+4
                    for k in range(j+1,min(d2,length)):
                        if int(s[j:k])<256:
                            if int(s[k:])<256:
                                if (s[k]=='0' and k==length-1) or s[k]!='0' :
                                    temp =s[:i]+'.'+s[i:j]+'.'+s[j:k]+'.'+s[k:]
                                    result.append(temp)
    print(result)

ss='010010'
restoreIpAddresses(ss)