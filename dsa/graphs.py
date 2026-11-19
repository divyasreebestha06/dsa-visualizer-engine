import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, u = heapq.heappop(pq)
        if curr_dist > distances[u]:
            continue
        for v, weight in graph[u].items():
            dist = curr_dist + weight
            if dist < distances[v]:
                distances[v] = dist
                heapq.heappush(pq, (dist, v))
    return distances

def bfs(graph, start):
    visited = []
    queue = [start]
    seen = {start}
    while queue:
        u = queue.pop(0)
        visited.append(u)
        for v in graph.get(u, []):
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return visited
