graph=[[0,10,3,0,0],[0,0,1,2,0],[0,4,0,8,2],[0,0,0,0,7],[0,0,0,9,0]]

def dijkstra(graph, s):
    dist = {}  # odległości
    for v in graph:
        dist[v] = float('inf')
    dist[s] = 0

    S = set()  # odwiedzone wierzchołki
    Q = set(graph.keys())  # kolejka

    while Q:
        u = min(Q, key=lambda x: dist[x])  # wybierz element z Q o minimalnej odległości
        Q.remove(u)
        S.add(u)

        for v in graph[u]:  # sąsiedzi wierzchołka u
            if dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]

    return dist
