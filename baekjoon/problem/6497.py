import sys
input = lambda: sys.stdin.readline().rstrip()
INF = sys.maxsize

def findRoot(parent, node):
  if node != parent[node]:
    parent[node] = findRoot(parent, parent[node])
  return parent[node]

def union(parent, node1, node2):
  node1 = findRoot(parent, node1)
  node2 = findRoot(parent, node2)

  if node1 < node2:
    parent[node2] = node1
  else:
    parent[node1] = node2

def solve(n, l):
  graph = [[*map(int, input().split())] for i in range(l)]
  parent = [i for i in range(n+1)]
  graph.sort(key=lambda x: x[2])
  result =0
  for i in graph:
    s, e, w = i

    if findRoot(parent, s) != findRoot(parent, e):
      union(parent, s, e)
    else:
      result += w

  return result


if __name__ == "__main__":
  for enter in sys.stdin:
    n, l = map(int, enter.split())
    if n == 0 and l == 0:
      break
    print(solve(n, l))