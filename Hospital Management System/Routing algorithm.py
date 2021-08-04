
import random

#NODES = 7

INVALID = 0.001

def next_node(s):
    nxt = []

    for i in range(NODES):
        if (distance_links[s][i] != INVALID):
            nxt.append(i)
    return nxt


def find_simple_paths(start, end):
    visited = set()
    visited.add(start)

    nodestack = list()
    indexstack = list()
    current = start
    i = 0

    while True:

        # get a list of the neighbors
        # of the current node
        neighbors = next_node(current)

        # Find the next unvisited neighbor
        # of this node, if any
        while i < len(neighbors) and neighbors[i] in visited:
            i += 1

        if i >= len(neighbors):
            visited.remove(current)

            if len(nodestack) < 1:
                break

            current = nodestack.pop()
            i = indexstack.pop()

        elif neighbors[i] == end:
            yield nodestack + [current, end]
            i += 1

        else:
            nodestack.append(current)
            indexstack.append(i + 1)
            visited.add(neighbors[i])
            current = neighbors[i]
            i = 0


def solution(sour, dest):
    block = 0
    l = []
    for path in find_simple_paths(sour, dest):
        l.append(path)

    k = 0
    for i in range(len(l)):
        su = 0
        for j in range(1, len(l[i])):
            su += (distance_links[l[i][j - 1]]
            [l[i][j]])
        k += su

    # print k
    dist_prob = []
    probability = []

    for i in range(len(l)):
        s, su = 0, 0

        for j in range(1, len(l[i])):
            su += (distance_links[l[i][j - 1]]
            [l[i][j]])

        dist_prob.append(su / (1.0 * k))

    for m in range(len(dist_prob)):
        z = (dist_prob[m])
        probability.append(z)

    for i in range(len(probability)):
        if (probability[i] == min(probability)):
            z = l[i]
            print("Shortest Path is ")
            print(z)

        # Driver Code


if __name__ == '__main__':
    
    NODES = int(input("Enter number of nodes : "))

    distance_links = [[INVALID for i in range(NODES)] for j in range(NODES)]

    c=1
    while(c==1):
        i = int(input("Enter the node 1 : "))
        j = int(input("Enter the node 2 : "))
        distance_links[i][j] = int(input("Enter the distance between 2 nodes: "))
        distance_links[j][i] = distance_links[i][j]
        c = int(input("Enter '1' to continue : "))
        
    source = int(input("Enter the source : "))
    dest = int(input("Enter the destination : "))
    solution(source, dest)