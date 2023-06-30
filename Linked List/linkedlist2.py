#Node Class 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#Linkedlist Class
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printlist(self):
        temp = self.head 
        if self.length >=1:
            for i in range(self.length):
                print("The element at position {} is {}".format(i+1, temp.value))
                temp = temp.next 

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node 
            self.tail = new_node 
        else:
            self.tail.next = new_node 
            self.tail = new_node 
            self.length += 1 
        return True 
    
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head

        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre 
        self.tail.next = None 

        self.length -= 1 

        if self.length == 0:
            self.head = None 
            self.tail = None 
        return temp.value 
    
    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node 
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node 

        self.length += 1
        return True 
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head 
        self.head = self.head.next
        temp.next = None 
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        
        return temp.value
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return False 
        temp = self.head
        for _ in range(index):
            temp = temp.next 

        return temp 
    
    def set_value(self, index, value):
        temp = self.get(index)
        if(temp):
            temp.value = value 
            return True 
        return False 
    
    def insert(self, index, value):
        if index < 0  or index > self.length:
            return False 
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index - 1)

        new_node.next = temp.next 
        temp.next = new_node
        self.length += 1
        return True 
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False 
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        pre = self.get(index - 1)
        temp = pre.next 
        pre.next = temp.next 
        temp.next = None

        self.length -= 1
        return temp.value 

        
        
    
    



if __name__ == '__main__':
    linkedlist = LinkedList(1)

    linkedlist.append(5)
    linkedlist.append(10)
    linkedlist.append(2)

    

    print("The last element deleted is {}".format(linkedlist.pop()))

    linkedlist.prepend(100)

    print("The first element deleted is {}".format(linkedlist.pop_first()))

    linkedlist.printlist()

    linkedlist.set_value(1,25)
    linkedlist.printlist()

    
    