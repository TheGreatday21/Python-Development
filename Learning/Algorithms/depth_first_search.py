
def dfs_stack (graph,start):
    visited = set()
    #we use a set because no data will be repeated and the values will be placed in a hash table , have hash values and time complexity O(1)- got on the first try 

    stack =[start]#assigning the variable to a stack

    while stack:
        node = stack.pop()#Removing the first file in the stack 
#we create a variable for our node of the graph 
        if node not in visited:#if the node is not in the set we print that node add add it to the set (visited)
            print (node, end= ",")# the "end = ' ' "is just to print the nodes in a row but there is spacing between them 
            visited .add(node) #adding the node to our visited set 

            for neighbor in reversed (graph [node]):
                if neighbor not in visited:
                    stack.append(neighbor)
# WE ENTER OUR DATA IN REVERSE BECAUSE OF STACKS LIFO (Last In First Out ) principle
#Your start node can be any of the nodes 
graph ={
    "A":["S","D"],
    "B":["S","D"],
    "C":["S","D"],
    "D":["A","B","C"],
    "S":["A","B","C"]
    
}
dfs_stack(graph,"S")




















