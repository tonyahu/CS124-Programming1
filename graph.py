# ----------------------------------------------------
# Harvard CS124 Programming 1. February 20, 2020.
# Submitted by Tony Hua & Jeffrey Lin
#
# RANDOM GRAPH MODULE
# Generates an matrix of edge lengths, with index i and j identifing nodes.
# ----------------------------------------------------


import random

def makeRandomGraph(dimension, numpoints):

    #create empty list of node coordinates
    nodeCordinates = []

    #init empty matrix of n x n 
    graph = [[0.0] * numpoints for i in range(numpoints)]

    # Case0: Complete graphs on n vertices, where the weight of each edge is a
    # real number chosen uniformly at random on [0, 1]
    if dimension == 0:
        print("Executing Case:", dimension)
        
        #insert random values as edges. Insert 0 if node points to itself.
        for i in range(numpoints):
            for j in range(numpoints):
                    if i == j:
                        graph[i][j] = 0.0
                    else:
                        graph[i][j] = random.random() 

        #flip values across diagonal
        for i in range(numpoints):
            for j in range(numpoints):
                graph[i][j] = graph[j][i]

        print(graph)
        return graph
        
    # Case2: Complete graphs on n vertices, where the vertices are points
    # chosen uniformly at random inside the unit square. (That is, the points
    # are (x, y), with x and y each a real number chosen uniformly at random
    # from [0, 1].) The weight of an edge is just the Euclidean distance
    # between its endpoints
    if dimension == 2:
        print("Executing case:", dimension)

        # Generate list of node and xy coordinates (bound between 0 and 1)
        for i in range (numpoints):
            x = random.random()
            y = random.random()
            nodeCordinates.append([x,y])

        #insert ecludian distance as edge based on x-y list. Insert 0 if node points to itself.
        for i in range(numpoints):
            for j in range(numpoints):
                    if i == j:
                        graph[i][j] = 0
                    else:
                        graph[i][j] =  (((nodeCordinates[j][0]-nodeCordinates[i][0])**2.0) + ((nodeCordinates[j][1]-nodeCordinates[i][1])**2.0))**(.5)

        #flip values across diagonal
        for i in range(numpoints):
            for j in range(numpoints):
                graph[i][j] = graph[j][i]

        print('Node XY Coordinates:',nodeCordinates)
        print('Graph:', graph)
        return graph




    # Case3: Complete graphs on n vertices, where the vertices are points
    # chosen uniformly at random inside the unit cube (3 dimensions)
    if dimension == 3:
        print("Executing case:", dimension)

        # Generate list of node and xyz coordinates (bound between 0 and 1)
        for i in range (numpoints):
            x = random.random()
            y = random.random()
            z = random.random()
            nodeCordinates.append([x,y,z])

        #insert ecludian distance as edge based on x-y list. Insert 0 if node points to itself.
        for i in range(numpoints):
            for j in range(numpoints):
                    if i == j:
                        graph[i][j] = 0
                    else:
                        graph[i][j] =  (((nodeCordinates[j][0]-nodeCordinates[i][0])**2.0) + ((nodeCordinates[j][1]-nodeCordinates[i][1])**2.0) + ((nodeCordinates[j][2]-nodeCordinates[i][2])**2.0))**(.5)

        #flip values across diagonal
        for i in range(numpoints):
            for j in range(numpoints):
                graph[i][j] = graph[j][i]

        print('Node XYZ Coordinates:',nodeCordinates)
        print('Graph:', graph)
        return graph



    # Case4: Complete graphs on n vertices, where the vertices are points
    # chosen uniformly at random inside the hyper cube (4 dimensions) 
    if dimension == 4:
        print("Executing case:", dimension)

        # Generate list of node and xyz coordinates (bound between 0 and 1)
        for i in range (numpoints):
            x = random.random()
            y = random.random()
            z = random.random()
            k = random.random()
            nodeCordinates.append([x,y,z,k])

        #insert ecludian distance as edge based on x-y list. Insert 0 if node points to itself.
        for i in range(numpoints):
            for j in range(numpoints):
                    if i == j:
                        graph[i][j] = 0
                    else:
                        graph[i][j] =  (((nodeCordinates[j][0]-nodeCordinates[i][0])**2.0) + ((nodeCordinates[j][1]-nodeCordinates[i][1])**2.0) + ((nodeCordinates[j][2]-nodeCordinates[i][2])**2.0) + ((nodeCordinates[j][3]-nodeCordinates[i][3])**2.0))**(.5)

        #flip values across diagonal
        for i in range(numpoints):
            for j in range(numpoints):
                graph[i][j] = graph[j][i]

        print('Node XYZK Coordinates:',nodeCordinates)
        print('Graph:', graph)
        return graph
    
    else:
        print('Error: Parameter error in makeRandomGraph(dimesion, numpoints). Please enter dimension of 0, 2, 3, or 4 only.')

