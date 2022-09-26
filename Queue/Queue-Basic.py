import queue


class Queue:
    def __init__(self) -> None:
        self.queuelist = []
        self.queuelength = 0

    def enqueue(self,data):
        self.queuelist.append(data)
        self.queuelength +=1
    
    def dequeue(self):
        if self.queuelength == 0:
            print('The queue is empty')
            return
        self.queuelist.pop(0)
        self.queuelength -=1

    def lastINQueue(self):
        if self.queuelength == 0:
            print("The queue is empty")
            return
        temp = self.queuelist[-1]
        print("Last element in the queue", temp)

    def traverse(self):
        if self.queuelength == 0:
            print("The queue is empty")
            return
        i = 0
        while i < self.queuelength :
            print("The queue elements ", self.queuelist[i])
            i+=1

           

    
    

if __name__ == '__main__':
    q =Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.traverse()
    q.dequeue()
    q.traverse()
    q.lastINQueue()
