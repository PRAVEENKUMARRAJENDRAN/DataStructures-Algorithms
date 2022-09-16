#Node class that as the data value and reference
from re import X


class Node:
    def __init__(self,data):
        self.item = data
        self.ref = None

#LinkedList Class
class LinkedList:
    def __init__(self):
        #At begining our linked list will have zero values, i.e. the start_node is None
        self.start_node = None

    def traverse_list(self):
        if self.start_node is None:
            print("No elements in the linked List")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item,"-->")
                n = n.ref

    def insert_at_start(self,data):
        #we will get the item and reference in the new_node
        new_node = Node(data)
        #we set the start_node to reference 
        self.ref = self.start_node
        #then we insert the new node to start_node
        self.start_node = new_node
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

    def insert_after_item(self,x,data):
        n = self.start_node
        while n is not None:
            if n.item == x:
                break 
            n = n.ref
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_before_item(self,x,data):
        #check whether the start_node is none or not 
        if self.start_node is None:
            print("The element is not present")
        #If the element is start node
        if x == self.start_node:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node

        #If the element is not start node 

        n =self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        
        if n.ref is None:
            print("Item ")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node 
    
    def insert_at_index(self,index,data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        
        i = 1
        n = self.start_node

        while i < index -1 and n is not None:
            n = n.ref
            i = i+1
        if n is None:
            print("Out of bound")
        else:
            new_node = Node(data)
            new_node.ref = n.ref 
            n.ref = new_node

    def getcount(self):
        n = self.start_node
        count = 0
        if n is None:
            print("The count is Zero")
        else:
            while n is not None:
                count = count + 1
                n = n.ref
            print(count)

    def searchElement(self,x):
        if self.start_node is None:
            print("No element is found")
            return
        
        n = self.start_node

        while n is not None:
            if n.item == x:
                print("The element is found")
                return True
            n = n.ref
        print("Item not found")
        return False

    def delete_at_start(self):
        if self.start_node is None:
            print("No elements to delete")
            return
        self.start_node = self.start_node.ref

    def delete_at_end(self):
        if self.start_node is None:
            print("No elements to delete")
            return
        n = self.start_node 

        while n.ref.ref is not None:
            n = n.ref
        n.ref = None 

    def delete_element_by_value(self,x):
        if self.start_node is None:
            print("No element to delete")
            return

        n = self.start_node

        if n.item == x:
            self.start_node = n.ref 
            return

        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref 

        if n.ref is None:
            print("No element to delete")
        else:
            n.ref = n.ref.ref

    def reverse_linkedlist(self):
        prev = None
        n = self.start_node
        while n is not None:
            next = n.ref
            n.ref = prev
            prev = n 
            n = next
        self.start_node = prev







            
        






if __name__ == "__main__":
    new_linked_list = LinkedList()
    new_linked_list.insert_at_start(20)
    new_linked_list.insert_at_end(5)
    new_linked_list.insert_at_end(10)
    new_linked_list.insert_at_end(15)

    new_linked_list.insert_after_item(10, 17)
    new_linked_list.insert_before_item(17, 25)
    new_linked_list.insert_at_index(3,8)
    new_linked_list.traverse_list()
    new_linked_list.getcount()
    new_linked_list.searchElement(10)


