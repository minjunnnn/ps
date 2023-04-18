import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    n, m = map(int, input().split())
    A = [[*map(int, input().split())] for i in range(n)]
    m, k = map(int, input().split())
    B = [[*map(int, input().split())] for i in range(m)]

    C = [[0 for i in range(n)] for i in range(k)]

    for i in range(n):
        for j in range(k):
            for z in range(m):
                C[i][j] += A[i][z] * B[z][j]

    for i in C:
        print(*i)



    

if __name__ == "__main__":
    solve()
