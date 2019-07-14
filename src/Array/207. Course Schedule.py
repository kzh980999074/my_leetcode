'''
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
Example 1:
Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
'''

def canFinish(numCourses,prerequisites):
    if not prerequisites:
        return True
    status=[1]*numCourses
    for i in prerequisites:
        status[i[0]]=0
    cans=set()
    j=len(prerequisites)
    for i in range(numCourses):
        if status[i]:
            cans.add(i)
    l=len(cans)
    if l==0:return False
    _j=-1
    print(cans)
    while not(l==0 or j==_j):
        _j=j
        _cans=set()
        i=0
        while i<j:
            if prerequisites[i][1] in cans:
                _cans.add(prerequisites[i][0])
                prerequisites[j-1],prerequisites[i]=prerequisites[i],prerequisites[j-1]
                j-=1
            else:
                i+=1
        i=0
        cans=_cans
        l=len(cans)
    if j==0:return True
    return False

a=[[1,0],[1,2],[0,1]]#False
print(canFinish(3,a))


        
        

