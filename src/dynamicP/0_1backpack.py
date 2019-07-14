



def backpack0_1(c,w,total_weight):
    '''c is a list represented price
    w is a list represented weight
    total_weight is the total weight that the packpack can accommodate
    '''
    w_c=[[0]*(len(c)+1) for _ in range(total_weight+1)]
    for i in range(len(c)):
        for j in range(1,total_weight+1):
            if j>=w[i]:
                w_c[j][i+1]= max(w_c[j-w[i]][i]+c[i],w_c[j][i] )
            else:
                w_c[j][i+1]=w_c[j][i]
    return w_c

c=[8,10,6,3,7,2]
w=[4,6,2,2,5,1]
p=backpack0_1(c,w,12)
for i in p:
    print(i)