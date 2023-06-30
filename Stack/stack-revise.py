
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_node = Node(value)

        if self.height == 0:
            self.top = new_node      
        else:
            new_node.next = self.top 
            self.top = new_node
        self.height += 1
        return True
    
    def pop_first(self):
        if self.height == 0:
            return False
        temp = self.top

        if self.height == 1:
            self.top = None
        else:
            self.top = temp.next
            temp.next = None 
        self.height -= 1
        return temp.value
    
    
    def print_stack(self):
        temp = self.top

        for i in range(self.height):
            print("The value of the stack at height {} is {}".format(i, temp.value))
            temp = temp.next




if __name__ == '__main__':
    stack = Stack(10)

    stack.push(45)

    stack.print_stack()
    print("The element that is deleted is {}".format(stack.pop_first()))