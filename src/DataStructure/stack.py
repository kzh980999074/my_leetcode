

class Stack:
    def __init__(self,length):
        self.A=[0]*length
        self.top=0
        self.length=length
    def stack_empty(self):
        if self.top==0:
            print('no element')
            return False
        return True
    def stack_full(self):
        if self.top==self.length:
            print('stack fulled')
            return True
        return False
    def pop(self):
        if self.stack_empty():
            self.top-=1
            print(self.A[self.top])
        return self.A[self.top]
    def push(self,key):
        if self.stack_full():
            print('can not push element')
            return 
        self.A[self.top]=key
        self.top+=1
        print('successed')
        return 

stack=Stack(10)
stack.pop()
stack.push(11)
stack.pop()