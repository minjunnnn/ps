import sys
input = lambda: sys.stdin.readline().rstrip()
min_ = float('inf')
INF = sys.maxsize

def solve():
    n = int(input())
    L = [*map(int, input().split())]
    dp = [0 for i in range(n + 1)]
    dp[0] = 0

    for idx, i in enumerate(L, start=1):
        for j in range(idx, n+1):
            
            dp[j] = max(dp[j - idx] + L[idx - 1], dp[j])
        
    return dp[n]

if __name__ == "__main__":
    print(solve())
