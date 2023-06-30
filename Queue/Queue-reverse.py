class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node 
        self.last = new_node 
        self.length = 1

    def print_queue(self):
        temp = self.first 

        for i in range(self.length):
            print("The element at the position {} is {}".format(i, temp.value))
            temp = temp.next 


    def enqueue(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.first = new_node
            self.last = new_node 
        else:
            self.last.next = new_node 
            self.last = new_node
        self.length += 1
        return True 
    
    def dequeue(self):
        if self.length == 0:
            return None 
        temp = self.first 
        if self.length == 1:
            self.first = None
            self.last = None 
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp.value 
    

if __name__ == '__main__':
    queue = Queue(23)

    queue.enqueue(29)
    queue.print_queue()