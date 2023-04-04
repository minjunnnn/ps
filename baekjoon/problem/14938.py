import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()
INF = sys.maxsize
max_ = -1

def dijkstra(start):
  global nodes, graph, rader, items, max_, INF
  distance = [INF] * (nodes + 1)
  pq = []
  heappush(pq, (0, start))
  distance[start] = 0
  
  while pq:
    cDist, cNode = heappop(pq)

    if cDist > distance[cNode]:
       continue
    
    for nNode, l in graph[cNode]:
      if distance[cNode] + l < distance[nNode]:
         distance[nNode] = distance[cNode] + l  
         heappush(pq, (distance[nNode], nNode))
  k = 0
  for i in range(1, nodes+1):
     if distance[i] <= rader:
       k += items[i-1]
        
  max_ = max(max_, k)  
  
def solve():
  global nodes, graph, rader, items
  nodes, rader, loads = map(int, input().split())
  items = [*map(int, input().split())]
  graph = [[] for i in range(nodes + 1)]
  for _ in range(loads):
     s, e, loadL = map(int, input().split())
     graph[s].append((e, loadL))
     graph[e].append((s, loadL))
  
  for i in range(1, nodes + 1):
     dijkstra(i)
  
        
if __name__ == "__main__":
  solve()
  print(max_)


# O(E^2log(V))