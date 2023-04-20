import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write
INF = sys.maxsize

def solve():
    n = int(input())
    mat = [[*map(int, input().split())] for i in range(n)]

    dp = [[INF for i in range(n)] for i in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for diff in range(n):
        for i in range(n - diff):
            for k in range(i, i+diff):
                dp[i][i+diff] = min(dp[i][i+diff], dp[i][k] + dp[k+1][i+diff] + mat[i][0] * mat[k][1] * mat[i+diff][1])

    print(dp[0][-1])

if __name__ == "__main__":
    solve()
