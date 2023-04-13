# prim's algorithm for minimum spanning tree
from heapq import heappop, heappush

def solve():
  vertex, edge = map(int, input().split())
  graph = [[] for i in range(vertex+1)]

  for i in range(edge):
    s, e, w = map(int ,input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))
  
  pq = []

  visited = [False] * (vertex+1)

  for end, weight in graph[1]:
    heappush(pq, (weight, end))
  
  visited[1] = True
  ans = 0  
  while pq:
    w_, e_ = heappop(pq)

    if visited[e_]:
      continue
      
    visited[e_] = True
    ans += w_ 

    for end_, weight_ in graph[e_]:
      heappush(pq, (weight_,end_))
  
  print(ans)
if __name__ == "__main__":
  solve()
    