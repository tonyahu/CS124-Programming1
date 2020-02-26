# ----------------------------------------------------
# Harvard CS124 Programming 1. February 20, 2020.
# Submitted by Tony Hua & Jeffrey Lin
#
# DELIVERABLES:
# input: ./randmst 0 numpoints numtrials dimension
# output: average numpoints numtrials dimension
# ----------------------------------------------------



# IMPORT MODULES
# ----------------------------------------------------
import graph as graph



# MAIN FUNCTION
# ----------------------------------------------------
def main(switch, numpoints, numtrials, dimension):
    
    #generate random graph
    graph.makeRandomGraph(dimension,numpoints)
    
    #Find MST
    #Import Jeff's Module here
    
    #Print results to console
    print("Program completed for the following input conditions:")
    average = 1
    print("Numpoints: %d" %numpoints)
    print("Numtrials: %d" %numtrials)
    print("Dimension: %d" %dimension)
    print("Average weight: %d" %average)


# INIT
# ----------------------------------------------------
if __name__ == "__main__": main(1,5,1,0)