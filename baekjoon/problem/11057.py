import sys
input = lambda: sys.stdin.readline().rstrip()
min_ = float('inf')
INF = sys.maxsize

def solve():
    n = int(input())
    L = [[0] * 11 for i in range(n + 1)]

    for i in range(1, 11):
        L[1][i] = L[1][i-1] + 1
    
    for i in range(2, n + 1):
        for j in range(1, 11):
          L[i][j] = (L[i][j-1] + L[i-1][j]) % 10007
    
    return L[-1][-1]
            
            


if __name__ == "__main__":
    print(solve())