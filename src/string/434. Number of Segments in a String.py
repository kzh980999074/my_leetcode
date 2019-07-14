'''
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
Please note that the string does not contain any non-printable characters.
Example:
Input: "Hello, my name is John"
Output: 5
'''
def countSegments(s):

    if not s :return 0
    finded=False
    length=len(s)
    position=0
    for i in range(length):
        if s[i].isalpha():
            finded=True
            position=i
            break
    if not finded:return 0
    count=1
    position+=1
    status=True
    while position<length:
        if status:
            if not (s[position].isalpha() or s[position]=='\'' or s[position]=='-'):
                status=False
            position+=1
        else:
            if s[position].isalpha():
                count+=1
                status=True
            position+=1
    return count
ss=", , , ,        a, eaefa"
print(countSegments(ss))
