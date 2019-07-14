'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Input: "()"
Output: true

Input: "()[]{}"
Output: true
'''
def isValid(s):
    if len(s)%2==1:return False 
    stack=[];
    dicts={'{':'}','[':']','(':')'}
    store=['{','[','(']
    for i in range(len(s)):
        if s[i] in store:
            stack.append(dicts[s[i]])
        else:
            if not stack:
                return False
            else:
                p=stack.pop();
                if not p==s[i]:
                    return False
    if not stack:
        return True
    else:
        return False
ss='()[]{}'
print(isValid(ss))

    