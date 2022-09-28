from multiprocessing.dummy import Manager


class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def getlevel(self):
        level = 0 
        p = self.parent

        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.getlevel() * 3
        prefix = spaces + "|-->" if self.parent else ""

        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree()

    

if __name__ == '__main__':
    RootNode = TreeNode('CEO')
    

    Manager1= TreeNode('M1')
    Manager1.add_child(TreeNode('E1'))
    Manager1.add_child(TreeNode('E1'))

    Manager2= TreeNode('M2')
    Manager2.add_child(TreeNode('E1'))
    Manager2.add_child(TreeNode('E1'))

    RootNode.add_child(Manager1)
    RootNode.add_child(Manager2)
    RootNode.add_child(TreeNode("Manager3"))
    RootNode.print_tree()



    
