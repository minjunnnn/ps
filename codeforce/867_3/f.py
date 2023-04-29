import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def dfs(v, count):
    global c, k, graph, visited, counts

    if visited[v]:
        return

    if count > c:
        c = count
        k = v
    visited[v] = True
    counts[v] = count
   
    for i in graph[v]:
        dfs(i, count + 1)

def solve():
    global c, k, graph, visited, counts
    n, kist, cost = map(int, input().split())
    graph = [[] for i in range(n + 1)]
    counts = [0] * (n + 1)
    visited = [False] * (n + 1)

    for i in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    c = 0
    k = 0
    dfs(1, 0)

    restore = [*counts]
    counts = [0] * (n + 1)
    kk = k
    c = 0
    k = 0
    visited = [False] * (n + 1)
    dfs(kk, 0)

    max_ = 0

    for i in range(1, n + 1):
        max_ = max(max_, counts[i] * kist - restore[i] * cost)

    return max_
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        print(solve())
