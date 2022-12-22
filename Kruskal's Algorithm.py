class Graph:
    def __init__(self, Vertices):
        self.V = Vertices
        self.graph = []

    def add_edge(self, U , V , W):
        self.graph.append([U , V , W])


    def Search(self, parent , i):
        if parent[i] == i:
            return i
        return self.Search( parent , parent[i])

    def apply_union(self , parent , rank, X , Y):
        X_root = self.Search( parent , X)
        Y_root = self.Search( parent , Y)
        if rank[X_root] < rank[Y_root]:
            parent[X_root] = Y_root
        elif rank[X_root] > rank[Y_root]:
            parent[Y_root] = X_root
        else:
            parent[Y_root] = X_root
            rank[X_root] += 1

    def Kruskal_Algorithm(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key = lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            U, V, W = self.graph[i]
            i = i + 1
            x = self.Search( parent , U)
            y = self.Search( parent , V)
            if x != y:
                e = e + 1
                result.append([U, V, W])
                self.apply_union( parent , rank , x , y)
                
        cost = 0
        for U, V, weight in result:
            cost += weight
            print("Edge","(",U,",",V,")",end =" ")
            print("weight =",weight)

        print("The total cost = " , cost)

     

g = Graph(4)
g.add_edge(0, 1 , 10)
g.add_edge(0 , 2 , 6)
g.add_edge(0 , 3 , 5)
g.add_edge(1 , 3 ,15)
g.add_edge(2 , 3, 4)

g.Kruskal_Algorithm()
