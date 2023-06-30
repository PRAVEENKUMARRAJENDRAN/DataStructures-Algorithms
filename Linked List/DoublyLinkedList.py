class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None 

class doublelinkedlist:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node 
        self.length = 1

    def printlist(self):
        temp = self.head

        for i in range(self.length):
            print("The element at position {} is {}".format(i+1, temp.value))
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail 
            self.tail.next = new_node
            self.tail = new_node 
        self.length += 1
        return True 
    
    def pop(self):
        if self.length == 0:
            return False 
        temp = self.tail 

        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            self.tail = temp.prev 
            temp.prev = None
            self.tail.next = None
        self.length -= 1    
        return temp.value 
    
    def append_first(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node 
            new_node.next = self.head 
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            self.head = None
            self.tail = None 
        temp = self.head 
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next 
            self.head.next = None
            temp.next = None 
        self.length -= 1
        return temp.value 
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return False 
        temp =  self.head 
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        print(temp.value)
        if temp:
            temp.value = value
            return True 
        return False 
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.append_first(value)
        elif index == self.length:
            return self.append(index)
        else:
            new_node = Node(value)
            before = self.get(index-1) ###elemnt before the index
            after = before.next #current index element 

            new_node.prev = before
            new_node.next = after
            before.next = new_node
            after.prev = new_node 
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)

        temp.prev.next = temp.next 
        temp.next.prev = temp.prev
        temp.prev = None
        temp.next = None 
        self.length -= 1
        return temp


    

if __name__ == '__main__':
    dlinkedlist = doublelinkedlist(2)

    dlinkedlist.append(5)

    print("The last element deleted is {}".format(dlinkedlist.pop()))

    dlinkedlist.append_first(100)
    print("The first element deleted is {}".format(dlinkedlist.pop_first()))
    dlinkedlist.append_first(20)
    print("The element at following index", dlinkedlist.get(1))
    dlinkedlist.set_value(1,500)
    dlinkedlist.insert(1,1000)
    print("The element removed is {}".format(dlinkedlist.remove(1)))
    dlinkedlist.printlist()

