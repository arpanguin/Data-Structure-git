import numpy as np
from Queues.QueueUsingArray import QueueUsingArray as Queue
from Stack.StackUsingArray import StackUsingArray as Stack


class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self.adj_matrix = np.zeros((self._vertices, self._vertices))
        self._visited = [0] * vertices

    def insert_edge(self, vertex1, vertex2, weight=1):
        """creating edge between origin i.e. vertex1 and destination i.e. vertex2"""
        self.adj_matrix[vertex1][vertex2] = weight

    def exist_edge(self, vertex1, vertex2):
        """:return if edge exist between origin i.e. vertex1 and destination i.e. vertex2"""
        return self.adj_matrix[vertex1][vertex2] != 0

    def remove_edge(self, vertex1, vertex2):
        """removing edge between origin i.e. vertex1 and destination i.e. vertex2"""
        self.adj_matrix[vertex1][vertex2] = 0

    def vertices(self):
        """print all the vertices"""
        for i in range(self._vertices):
            print(i, end=' ')
        print()

    def edges(self):
        """print all the edges"""
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self.adj_matrix[i][j] != 0:
                    print(f"{i} ==> {j}")

    def vertex_count(self):
        """:return number of vertex exist in the graph"""
        return self._vertices

    def edge_count(self):
        """:return number of edges exist in the graph"""
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self.adj_matrix[i][j] != 0:
                    count += 1
        return count

    def indegree(self, vertex):
        """:returns the indegree of vertex"""
        count = 0
        for i in range(self._vertices):
            if self.adj_matrix[i][vertex] != 0:
                count += 1
        return count

    def outdegree(self, vertex):
        """:returns the outdegree of vertex"""
        count = 0
        for i in range(self._vertices):
            if self.adj_matrix[vertex][i] != 0:
                count += 1
        return count

    def display(self):
        """display the graph in matrix format"""
        print(self.adj_matrix)

    def BFS(self, vertex):
        """Traversing using Breadth First Search.
            It is a vertex based technique for finding a shortest path in graph. It uses a Queue data structure
            which follows first in first out. In BFS, one vertex is selected at a time when it is visited and marked
            then its adjacent are visited and stored in the queue. It is slower than DFS.
            It is similar as level order search in tree.
        """
        i = vertex
        queue = Queue()
        visited = [0] * self._vertices
        print(i, end=" ")
        visited[i] = 1
        queue.enqueue(i)
        while not queue.is_empty():
            i = queue.dequeue()
            for j in range(self._vertices):
                if self.adj_matrix[i][j] != 0 and visited[j] == 0:
                    visited[j] = 1
                    queue.enqueue(j)
                    print(j, end=" ")

    def DFS(self, vertex):
        """Depth First Search
           It is a edge based technique. It uses the Stack data structure, performs two stages, first
            visited vertices are pushed into stack and second if there is no vertices then visited
            vertices are popped.
        """
        if self._visited[vertex] == 0:
            print(vertex, end=' ')
            self._visited[vertex] = 1
            for j in range(self._vertices):
                if self.adj_matrix[vertex][j] == 1 and self._visited[j] == 0:
                    self.DFS(j)


print("\n\nGraph")
graph = Graph(8)
graph.insert_edge(1, 2)  # here indegree vertices will be 2 and outdegree will be 1 and 3rd param is to add weight
graph.insert_edge(1, 3)
graph.insert_edge(2, 3)
graph.insert_edge(2, 4)
graph.insert_edge(2, 6)
graph.insert_edge(3, 5)
graph.insert_edge(6, 7)
graph.display()
print(f"\nNumber of edges : {graph.edge_count()}")
print("\nVertices....")
graph.vertices()
print("\nEdges exists between....")
graph.edges()
print(f"\nIndegree of vertex : {graph.indegree(2)}")
print(f"\nOutdegree of vertex : {graph.outdegree(1)}")
print(f"\nTraverse using BFS")
graph.BFS(1)
print(f"\nTraverse using DFS")
graph.DFS(1)
