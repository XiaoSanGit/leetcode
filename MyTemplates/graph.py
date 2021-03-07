import heapq

def dijstra(graph,start,end):
    heap = [(start,0)]
    visited = set()
    while heap:
        (node,cost) = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        if node == end:
            return cost
        for v,c in graph[node]:
            if v in visited:
                continue
            next_cost = cost + c
            heapq.heappush(heap,(v,next_cost))
    return -1



def floyd_warshall(graph, v):
    dist = [[float("inf") for _ in range(v)] for _ in range(v)]

    for i in range(v):
        for j in range(v):
            dist[i][j] = graph[i][j]

    # check vertex k against all other vertices (i, j)
    for k in range(v):
        # looping through rows of graph array
        for i in range(v):
            # looping through columns of graph array
            for j in range(v):
                if (
                        dist[i][k] != float("inf")
                        and dist[k][j] != float("inf")
                        and dist[i][k] + dist[k][j] < dist[i][j]
                ):
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist, v