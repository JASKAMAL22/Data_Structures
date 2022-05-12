import queue
class MyStack:

    def __init__(self):
        self.q1=queue.Queue()
        self.q2=queue.Queue()
        self.c=0
        
        

    def push(self, x: int) -> None:
        self.c+=1
        self.q2.put(x)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        
        self.q=self.q1
        self.q1=self.q2
        self.q2=self.q
        
        

    def pop(self) -> int:
        if self.empty():
            return -1
        d=self.q1.get()
        self.c-=1
        return d
        

    def top(self) -> int:
        return self.q1.queue[0]
        

    def empty(self) -> bool:
        return self.c==0
      
      
'''
Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid. '''

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
