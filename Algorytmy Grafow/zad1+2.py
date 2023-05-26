def BFS(graph, s):
    Q=[]
    colors=[0]*len(graph)
    colors[s]=1
    Q.append(s)
    while len(Q)!=0:
        u=Q[0]
        sasiadi=graph[u]
        for v in range(len(sasiadi)):
            if colors[v]==0 and sasiadi[v]==1:
                colors[v]=1
                Q.append(v)
                print(u,">",v)
    Q.pop(0)
    colors[u]=2
graph=[[0,1,1,1,0,1],[0,0,0,0,1,0],[0,1,0,0,0,0],[0,0,0,0,0,1],[0,0,0,0,0,0],[0,0,1,0,1,0]]
BFS(graph,0)

def bfs_list(lista,s):
    Q=[]
    colors = [0]*len(graph)
    colors[s]=1
    Q.append(s)
    while len(Q)!=0:
        u=Q[0]
        sasiadi=graph[u]
        for v in range(len(sasiadi)):
            if colors[v]==0:
                colors[v]=1
                Q.append(v)
    Q.pop(0)
    colors[u]=2
bfs_list(graph,0)