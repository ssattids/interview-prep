# %%
import queue


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            # self.vertices[v2].add(v1)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def __str__(self):
        return str(self.vertices)


my_graph = Graph()
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_vertex(4)
my_graph.add_vertex(5)

my_graph.add_edge(1, 2)
my_graph.add_edge(2, 3)
my_graph.add_edge(3, 1)
my_graph.add_edge(1, 4)
my_graph.add_edge(4, 5)

# %%
v1 = 1
v2 = 5

my_que = []
my_que.append(1)
flag_execute = True
while my_que != []:
    v = my_que.pop(0)
    if v == v2:
        print("A path exists")
        flag_execute = False
        break
    for i in my_graph.get_neighbors(v):
        if i not in my_que:
            my_que.append(i)
if flag_execute:
    print("A path does not exist")
    

# %%
4