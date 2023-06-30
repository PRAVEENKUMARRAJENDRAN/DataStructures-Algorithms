class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            print(self.adj_list)
            return True
        
        return False 
    
    def add_edge(self, v1, v2):
        
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            if v1 not in self.adj_list[v2] and v2 not in self.adj_list[v1]:
                self.adj_list[v1].append(v2)
                self.adj_list[v2].append(v1)
                return True 
        return False 
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False 
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for other_vertex in self.adj_list[vertex]:
                if other_vertex in self.adj_list:
                    self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True 
        return False 
    
    def print_graph(self):
        v_list = []
        for vertex in self.adj_list:
            v_list.append(vertex)
        v_list.sort()
        for v in v_list:
            print(v, ':', self.adj_list[v])
    
    
    


if __name__ == '__main__':
    G = Graph()
    G.add_vertex(2)
    G.add_vertex(3)
    G.add_vertex(6)

    G.add_edge(3, 2)
    G.add_edge(6, 2)
    G.add_edge(6, 3)
    G.add_edge(6, 3)
    print(G.adj_list)
    G.print_graph()
