class Stack:
    def __init__(self) -> None:
        self.stacklist = []
        self.stacksize = 0

    def push(self,element):
        self.stacklist.append(element)
        self.stacksize += 1
    def traverse(self):
        i = 0
        if self.stacksize == 0:
            print('The stack is empty')
            return
        while i < self.stacksize:
            print('The Stack elements are',self.stacklist[i])
            i+= 1
    def pop(self):
        if self.stacksize == 0:
            print('The stack is empty we cannot perform pop')
            return
        temp = self.stacklist.pop()
        self.stacksize -=1
        return temp




if __name__ == '__main__':
    S = Stack()
    S.push(1)
    S.push(2)
    S.traverse()
    S.pop()
    S.traverse()
