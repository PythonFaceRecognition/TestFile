'''import os
# the folder containing all the input data
input_folder = 'C:\\Users\\USER\\Desktop\\Face_Test_photo\\CBSR_database\\test_release\\test_release'
# the folder to store the output results
#output_folder = 'C:\\Users\\USER\\Desktop\\Face_Test_photo\\CBSR_database'

# list all the item of the input folder
items = os.listdir(input_folder)
# make all the items full-path
for i in range(len(items)):
    items[i] = '{0}\\{1}'.format(input_folder, items[i])

while len(items) > 0:
    # pop the first folder from folders
    item = items.pop(0)
    # check the type of the item
    if os.path.isdir(item):
        # the item is type of folder so append it to folders
        # print('folder: {0}\n'.format(item))
        # list all the items in the item
        sub_items = os.listdir(item)
        for i in range(len(sub_items)):
            items.append('{0}\\{1}'.format(item, sub_items[i]))
    elif os.path.isfile(item) :
        # the item is type of file so append it to folders
        print('file: {0}'.format(item))
#include<iostream>
#include<opencv.hpp>'''

''' Array = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}


# visits all the nodes of a Array (connected component) using BFS
def bfs_connected_component(Array, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]

    position = {}         # this dict keeps track of levels
    position[start]= 0    # depth of start node is 0

    visited= [start]     # to avoid inserting the same node twice into the queue

    # keep looping until there are nodes still to be checked
    while queue:
       # pop shallowest node (first node) from queue
        node = queue.pop(0)
        explored.append(node)
        neighbours = Array[node]

        # add neighbours of node to queue
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

                position[neighbour]= position[node]+1
                # print(neighbour, ">>", levels[neighbour])

    print(position)

    return explored

ans = bfs_connected_component(Array,'A') # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']
print(ans)
print ("BFS Search")'''




graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n, visited)
    return visited

visited = dfs(graph1,'A', [])
print(visited)
print ("DFS Search")
