def permutation(n):
    if n<=0: return []
    result=[[0]]
    i=1
    while i<n:
        temp=[]
        while result:
            var=result.pop()
            for j in range(i+1):
                new_element=var[:j]+[i]+var[j:]
                temp.append(new_element)
        result=temp
        i+=1
    return result
print(len(permutation(4)))
        
