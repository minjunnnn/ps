import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
  n, m = map(int, input().split())
  p = [[*map(int, input().split())] for i in range(m)]

  check = [-1 for i in range(n+1)]

  for idx, p in enumerate(p):
    for i in range(p[0], p[1] + 1):
       check[i] = idx
  
  a = set()
  for i in check:
    if i >= 0:
       a.add(i)
  
  return 2 ** len(a)

if __name__ == "__main__":
    print(solve())
