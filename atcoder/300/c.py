import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]

def check(x, y):
    global L, h, w, visited, maxN
    if L[x][y] != '#' or visited[x][y]:
        return -1

    

    for i in range(maxN):
        visitStore = []
        for j in range(4):
            nx = x + dx[j] * (i + 1)
            ny = y + dy[j] * (i + 1)

            if nx < 0 or ny < 0 or nx >= h or ny >= w or visited[nx][ny]:
                return i - 1
            
            if L[nx][ny] == '#':
                visitStore.append((nx, ny))
                continue
            else:
                return i - 1
        for zx, zy in visitStore:
            visited[zx][zy] = True

        
    return h - 1


def solve():
    global L, h, w, visited, maxN
    h, w = map(int, input().split())
    maxN = max(h, w)
    L = [list(input()) for i in range(h)]
    visited = [[False for i in range(w)] for i in range(h)]

    result = [0] * h

    for i in range(h):
        for j in range(w):
            k = check(i, j)
            if k == -1:
                continue
            else:
                result[k] += 1
    
    return result


if __name__ == "__main__":
    print(*solve())
