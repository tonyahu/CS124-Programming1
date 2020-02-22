# Harvard CS124 Programming 1. February 20, 2020.
# Submitted by Tony Hua

####### Assignment objectives ########
# For each case, determine how the expected (average) weight of the minimum spanning tree (not an edge, the whole MST) grows as a function of n

####### Cases ##########
#Case1: Complete graphs on n vertices, where the weight of each edge is a real number chosen uniformly at random on [0, 1]

#Case2:  Complete graphs on n vertices, where the vertices are points chosen uniformly at random inside the unit square. (That is, the points are (x, y), with x and y each a real number chosen uniformly at random from [0, 1].) The weight of an edge is just the Euclidean distance between its endpoints

#Case3:  Complete graphs on n vertices, where the vertices are points chosen uniformly at random inside the unit cube (3 dimensions) and hypercube (4 dimensions). As with the unit square case above, the weight of an edge is just the Euclidean distance between its endpoints


####### Deliverables #########
# input: ./randmst 0 numpoints numtrials dimension
# output: average numpoints numtrials dimension









#tips from lecture7
#path compression: instead of jumping through multiple pathways to find root, we just re-assign a new pathway directly pointing to root. At a constant cost of that extra step, we save ourselves the possibility of a larger magnitude cost with large pathways.


#helper functions



def makeRandomGraph(dimension, numpoints):
    if dimension == 0:
        print("Case 1 chosen")
        #
        #
        #

    if dimension == 2:
        print("Case 2 chosen")
    if dimension == 3:
        print("Unit cube chosen")
    if dimension == 4:
        print("Hypercube chosen")
    else:
        print("Error: Please input value 0,2,3, or 4 for dimension.")
    


def makeSet(x):
        print("makeSet")
        parent[x] = x #set parent pointer to itself
        rank[x] = 0 #set rank to 0


def rank(x):
    """ keeps track of 'height' of each mini tree or set. we want shorter trees to point towards taller trees to maintain a shorter path length back to root """
    #
    #
    #

def find(x):
    """finds name of a set"""
    #
    #

def link(x,y):
    """links sets x and y together. Shorter set is linked to longer set"""
    #
    #
    #

def union(x,y):
    #

def kruskalMST(set):
    parent = []
    rank = []




def main():
    print("Running main code")





if __name__ == '__main__':main()