# Harvard CS124 Programming 1. February 20, 2020.
# Submitted by Tony Hua

####### Assignment objectives ########
# For each case, determine how the expected (average) weight of the minimum spanning tree (not an edge, the whole MST) grows as a function of n

####### Cases ##########
#Case1: Complete graphs on n vertices, where the weight of each edge is a real number chosen uniformly at random on [0, 1]

#Case2: Complete graphs on n vertices, where the vertices are points chosen uniformly at random inside the unit square. (That is, the points are (x, y), with x and y each a real number chosen uniformly at random from [0, 1].) The weight of an edge is just the Euclidean distance between its endpoints

#Case3: Complete graphs on n vertices, where the vertices are points chosen uniformly at random inside the unit cube (3 dimensions) and hypercube (4 dimensions). As with the unit square case above, the weight of an edge is just the Euclidean distance between its endpoints


####### Deliverables #########
# input: ./randmst 0 numpoints numtrials dimension
# output: average numpoints numtrials dimension









#tips from lecture7
#path compression: instead of jumping through multiple pathways to find root, we just re-assign a new pathway directly pointing to root. At a constant cost of that extra step, we save ourselves the possibility of a larger magnitude cost with large pathways.



##### IMPORT ######
import numpy as np

##### FUNCTIONS #####




class graph:
    def __init__(self, dimensionType, numpoints):
       self.dimensionType = dimensionType
       self.numpoints = numpoints
       self.graph = []

    def addEdge(self,u,v,w):
       self.graph.append([u,v,w]) 

    #make a new set at each node. Each set consists of parent identifiers and ranking
    def makeSet(self, node):
        parent[node] = node #set parent pointer to itself
        rank[node] = 0 #set node rank to 0

    #recursively goes up tree until root is located. Then returns root.
    def find(self, parent, node): 
		if parent[node] == node: #if node is a root, we are done. return the value.
            return node 
		return self.find(parent, parent[node]) #else, keep going upwards.

    #links a small tree to larger tree. Increases its rank, and returns the new larger tree
    def link(self, node1, node2):
        if rank[node1] > rank[node2]:
            temp = node1 
            node1 = node2   #we swap values of node1 ↔ node2
            node2 = temp
        if rank[node1] == rank[node2]:
            rank[node2] = rank[node2] +1    #if node ranks are same, then we increase rank node2. Else, node2 should have higher rank than node1 already from swap.
        parent[x] = node2   #then we increase rank of node1 to match node2 after linking.
        return node2


    def makeRandomGraph(self, dimension, numpoints):
        graph = [] #init empty graph

        if dimension == 0:
            print("Generating graph for case 1.")
            #for numpoints:
                #addEdge(u,v,rand(w,0,1))
                #

        if dimension == 2:
            print("Generating random graph for case 2, unit square")
            #for numpoints, generate rand vertices inside unit square. weights are calculated based on pythagorean theorem
            #for numpoints,
                #temp coordinates
                #ux=rand(0,1)
                #uy=rand(0,1)
                #vx=rand(0,1)
                #vy=rand(0,1)
                #addEdge(u,v,w=sqrt((vx-ux)^2+(vy-uy)^2))
                #edge weights calculated via pythagorean theorem

        if dimension == 3:
            print("Generating random graph for case 3, a cube")
            #for numpoints, generate rand xyz vertices inside cube. weights are calculated based on pythagorean theorem
            #for numpoints,
                #temp coordinates
                #ux=rand(0,1)
                #uy=rand(0,1)
                #uz=rand(0,1)
                #vx=rand(0,1)
                #vy=rand(0,1)
                #vz=rand(0,1)
                #addEdge(u,v,w=sqrt((vx-ux)^2+(vy-uy)^2)+(vz-uz)^2))
                #edge weights calculated via pythagorean theorem

        if dimension == 4:
            print("Generating random graph for case 4, a HYPER cube")
            #for numpoints, generate rand xyzk vertices inside unit square. weights are calculated based on pythagorean theorem
            #for numpoints,
                #temp coordinates
                #ux=rand(0,1)
                #uy=rand(0,1)
                #uz=rand(0,1)
                #uk=rand(0,1)
                #vx=rand(0,1)
                #vy=rand(0,1)
                #vz=rand(0,1)
                #vk=rand(0,1)
                #addEdge(u,v,w=sqrt((vx-ux)^2+(vy-uy)^2)+(vz-uz)^2)+(vk-uk)^2))
                #edge weights calculated via pythagorean theorem
        else:
            print("Error: Please input value 0,2,3, or 4 for dimension. Life is hard as is already. Please don't make it harder.")
        















def kruskalMST(graphToOptimize):
    parent = []
    rank = []




def main():
    print("Running main code")


if __name__ == '__main__':main()