import sys
input = lambda: sys.stdin.readline().rstrip()
INF = sys.maxsize
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def solve():
  n = int(input())
  L = [[*map(int, input().split())] for i in range(2)]

  dp = [[0] * (n+1) for i in range(3)]

  for i in range(1,n+1):
    for j in range(3):
      if j == 0:
        dp[j][i] = max(dp[1][i-1], dp[2][i-1])
      elif j == 1:
        dp[j][i] = max(dp[0][i-1] + L[0][i-1], dp[2][i-1] + L[0][i-1])
      else:
        dp[j][i] = max(dp[0][i-1] + L[1][i-1], dp[1][i-1] + L[1][i-1])

  return max(dp[0][-1], dp[1][-1], dp[2][-1])

if __name__ == "__main__":
  T = int(input())
  for i in range(T):
     print(solve())