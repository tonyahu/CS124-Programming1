#Harvard CS124 Programming 1
#By Tony Hua



#tips from lecture7

#path compression: instead of jumping through multiple pathways to find root, we just re-assign a new pathway directly pointing to root. At a constant cost of that extra step, we save ourselves the possibility of a larger magnitude cost with large pathways.


#helper functions

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
