#  File: Adjacency.py
#  Description: Converts an edge list into an adjacency matrix
#  Student Name: Alec Anaya
#  Student UT EID: aa89468
#  Course Name: CS 313E
#  Unique Number:

def edge_to_adjacency(edge_list):
# Add Your code here!
   
    scheme = []
    for i in edge_list:
        if i[0] not in scheme:
            scheme.append(i[0])
    for j in edge_list:
        if j[1] not in scheme:
            scheme.append(j[1])
    scheme.sort()
    matrix = [[0 for c in range(len(scheme))]for r in range(len(scheme)) ]
            
    for c in edge_list:
        for r in c:
            matrix[scheme.index(c[0])][scheme.index(c[1])]=c[-1]
    return matrix
        
            
                
                


# ------ DO NOT CHANGE BELOW HERE ------ #
import ast

def main():
    matrix = edge_to_adjacency(ast.literal_eval(input()))

    print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))

if __name__ == "__main__":
    main()
