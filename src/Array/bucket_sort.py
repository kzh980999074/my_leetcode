
#桶排序:
#输入:带排序数组A 并且假设 A中的元素 在[0,1]之间
#idea:需要一个临时数组B 存放bucket,如果需要n个桶  则A中元素i在 A[i]*n 取整  的桶中

def bucket_sort(A):
    n=len(A)
    B=[[] for i in range(n)]
    print(B)
    for i in A:
        B[int(i*n)].append(i)
    print(B)
    for i in range(n):
        B[i].sort()
    j=0
    for i in range(n):
        for k in B[i]:
            A[j]=k
            j+=1
    print(A)
    return A
A=[0.79,0.13,0.16,.64,0.39,0.20,0.89,0.53,0.71,0.42]
bucket_sort(A)