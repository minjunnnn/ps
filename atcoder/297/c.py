import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    h, w = map(int, input().split())
    L = [list(input()) for i in range(h)]

    visited = [[False for i in range(w)]for i in range(h)]
    for i in range(h):
        for j in range(w-1):
            if L[i][j] == 'T' and not visited[i][j]:
                if L[i][j+1] == 'T':
                    L[i][j] = 'P'
                    L[i][j+1] = 'C'
                    visited[i][j] = True
                    visited[i][j+1] = True
    
    for i in range(h):
        print(*L[i],sep="")





if __name__ == "__main__":
    solve()
