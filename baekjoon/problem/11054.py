import sys
input = lambda: sys.stdin.readline().rstrip()
INF = sys.maxsize

def solve():
  n = int(input())
  L = [*map(int, input().split())]

  dp = [1] * n

  for i in range(len(L)):
    for j in range(i):
      if L[j] < L[i]:
        dp[i] = max(dp[j] + 1, dp[i])

  for i in range(len(L)):
    for j in range(i):
      if L[j] > L[i]:
        dp[i] = max(dp[j] + 1, dp[i])

  return max(dp)

if __name__ == "__main__":
    print(solve())