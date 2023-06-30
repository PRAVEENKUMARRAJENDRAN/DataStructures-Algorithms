class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        for i in range(self.length):
            print("The element at position " + str(i + 1) + " is " + str(temp.value))
            temp = temp.next

    def append(self,value):
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
        return temp 
    
    def prepend(self,value):
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
            return False
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return False
        temp = self.head

        for _ in range(index):
            temp = temp.next

        return temp
    
    def set_value(self,index,value):
        temp = self.get(index)
        if(temp):
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.append(value)
        if index == self.length:
            return self.prepend(value)
        
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next 
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()
        
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None

        self.length -= 1
        return temp.value
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before 
            before = temp 
            temp = after  
        


LL = LinkedList(1)

# LL.print_list()

LL.append(2)
LL.append(3)

# LL.print_list()

LL.pop()
# LL.print_list()
LL.pop()
# LL.print_list()
LL.prepend(5)
# LL.print_list()
LL.pop_first()
LL.append(2)
LL.append(3)
# LL.print_list()

LL.set_value(1,10)
LL.print_list()
LL.insert(2,90)
LL.reverse()
LL.print_list()
    

