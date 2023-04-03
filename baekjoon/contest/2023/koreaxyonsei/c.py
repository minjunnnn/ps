# 27932
import sys
input = lambda: sys.stdin.readline().rstrip()

def check(v):
  global t, k
  tired = 0
  for i in t:
    flag = True
    for j in i:
      if j > v:
        flag = False
    
    if not flag:
      tired += 1
  if tired > k:
    return False
  else:
    return True

def solve():
  global t, k
  n, k = map(int, input().split())
  L = [*map(int, input().split())]
  t = []

  if n == 1:
    return 0

  for idx, i in enumerate(L):
    if idx == 0:
      t.append([abs(L[idx + 1] - L[idx])])
    elif idx == n-1:
      t.append([abs(L[idx] - L[idx-1])])
    else:
      t.append((abs(L[idx+1] - L[idx]), abs(L[idx] - L[idx-1])))
  l = 0
  max_ = -1
  for i in t:
    for j in i:
      max_ = max(max_, j)
  r = max_
  while l + 1 < r:
    mid = (l + r) >> 1
    if check(mid):
      r = mid
    else:
      l = mid
  if check(l):
    return l
  else:
    return r
    
if __name__ == "__main__":
    print(solve())