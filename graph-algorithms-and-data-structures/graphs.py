#!/usr/bin/env python3

class EmptyGraphError(Exception):
    """Exception raised when an repesentation operation is attempted on an empty graph."""
    pass

class NodeNotFoundError(Exception):
    """Exception raised when a node is not found in the graph."""
    pass

class NodeAlreadyExistsError(Exception):
    """Exception raised when trying to add a node that already exists in the graph."""
    pass


class Grpah:
    #constructor for the Graph class
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()


    #representation of the graph as a string
    def __repr__(self):

        try:
            sum = 0
            for _ in self.adj_list.keys():
                sum += 1
            if sum == 0:
                raise EmptyGraphError
            else:
                graph_str = "Graph:\n"
                for node, neighbors in self.adj_list:
                    graph_str += f"{node} -> {neighbors}\n"
                return graph_str
        
        except EmptyGraphError: 
            return 1


    #add a node to the graph
    def add_node(self, node):

        try:
            if node not in self.adj_list:
                self.adj_list[node] = []
                return 0
            else:
                raise NodeAlreadyExistsError
        
        except NodeAlreadyExistsError:
            print(f"\nNode {node} already exists in the graph.")
            return 1

    #remove a node from the graph
    def remove_node(self, node):

        try:
            if node in self.adj_list:
                del self.adj_list[node]
                for neighbors in self.adj_list.values():
                    if node in neighbors:
                        neighbors.remove(node)
                return 0
            else:
                raise NodeNotFoundError
         
        except NodeNotFoundError:
            print(f"\nNode {node} does not exist in the graph.")
            return 1
        
    
    #add an edge from one node to another
    def add_edge(self, from_node, to_node, weight=None):

        if from_node not in self.adj_list:
            self.add_node(from_node)
        
        if to_node not in self.adj_list:
            self.add_node(to_node)
        
        if weight is None:
            self.adj_list[from_node].append(to_node)
            if not self.directed:
                self.adj_list[to_node].append(from_node)
        else:
            self.adj_list[from_node].append((to_node, weight))
            if not self.directed:
                self.adj_list[to_node].append(from_node, weight)
        return 0
        

    #remove an edge from one node to another
    def remove_edge(self, from_node, to_node):
        
        try:
            if from_node in self.adj_list and to_node in self.adj_list[from_node]:
                self.adj_list[from_node].remove(to_node)
                if not self.directed:
                    self.adj_list[to_node].remove(from_node)
                return 0
            else:
                raise NodeNotFoundError

        except: 
            print(f"\nEdge from {from_node} to {to_node} does not exist in the graph.")
            return 1


    #get the neighbors of a node
    def get_neighbors(self, node):

        try:
            if node in self.adj_list:
                return self.adj_list[node]
            else:
                raise NodeNotFoundError
        
        except NodeNotFoundError:
            print(f"\nNode {node} does not exist in the graph.")
            return None


    #check if a node exists in the graph
    def has_node(self, node):

        if node in self.adj_list:
            return True
        else:
            return False


    #check if an edge exists between two nodes
    def has_edge(self, from_node, to_node):

        if from_node in self.adj_list and to_node in self.adj_list:
            if to_node in self.adj_list[from_node]:
                return True
            else:
                return False
        else:
            return False


    #get all nodes in the graph
    def get_nodes(self):
        return list(self.adj_list.keys())


    #get all edges in the graph
    def get_edges(self):
        edges = []
        for from_nodes, neighbors in self.adj_list.items():
            for to_node in neighbors:
                edges.append((from_nodes, to_node))
        return edges


    #get the number of nodes in the graph in the BF order
    def BFS(self, start_node):
        visited = set()
        queue = [start_node]
        order = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_neighbors(node)
                for neighbor in neighbors:
                    if neighbor not in visited:
                        if isinstance(neighbor, tuple):
                            neighbor = neighbor[0]
                        else:
                            neighbor = neighbor
                        queue.append(neighbor)
        return order


    #get the number of nodes in the graph in the DF order
    def DFS(self, start_node):
        visited = set()
        stack = [start_node]
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_neighbors(node)
                for neighbor in neighbors:
                    if neighbor not in visited:
                        if isinstance(neighbor, tuple):
                            neighbor = neighbor[0]
                        else:
                            neighbor = neighbor
                        stack.append(neighbor)
        return order
    

def main():
    
    g = Grpah(directed=True)  # Correctly define the graph object

    g.add_edge('A', 'B')
    g.add_edge('A', 'C', 10)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 1)
    g.add_edge('D', 'C', 1)
    g.add_edge('A', 'E', 1)
    g.add_edge('E', 'F', 1)
    g.add_edge('G', 'F', 1)
    g.add_edge('F', 'H', 1)
    g.add_edge('H', 'I', 1)
    g.add_edge('I', 'G', 100)

    print(f"Graph's nodes: {g.get_nodes()}")
    print(f"BFS from 'A': {g.BFS('A')}")
    print(f"DFS from 'A': {g.DFS('A')}")

    return 0

if __name__ == "__main__":
    main()