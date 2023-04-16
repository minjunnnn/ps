import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write
INF = sys.maxsize
def solve():
    n, m, a, b = map(int, input().split())
    closed = [True] * (n + 1)
    dp = [0] + [INF] * n

    for i in range(m):
        s, e = map(int, input().split())

        for j in range(s, e + 1):
            closed[j] = False
    
    ma = min(a, b)
    mb = max(a, b)


    for _ in range(100):
      for i in range(ma, n+1):
          if not closed[i] or not closed[i - ma]:
              continue
          dp[i] = min(dp[i], dp[i - ma] + 1)
      for i in range(mb, n+1):
          if not closed[i] or not closed[i - mb]:
              continue
          dp[i] = min(dp[i], dp[i - mb] + 1)

    print(-1 if dp[n] == INF else dp[n])

if __name__ == "__main__":
    solve()
