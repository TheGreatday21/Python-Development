from collections import deque
#allows us to append and pop from either ends of the queue

def bfs(graph,start):
    visited = set()#keep track of the visited nodes

    queue = deque([start])

    output = []#this empty list to display our nodes in terminal in the order they were traversed

    while queue :
        node = queue.popleft()
        if node not in visited:
            print(node, end = ",")
            
            visited.add(node)#adds the nodes to the set 

            output.append(node)#adds the nodes to the list

            for neighbor in (graph [node]):
                if neighbor not in visited:
                    queue.append(neighbor)

graph ={
    "A":["S","D"],
    "B":["S","D"],
    "C":["S","D"],
    "D":["A","B","C"],
    "S":["A","B","C"]
    
}

bfs(graph,"S")
































