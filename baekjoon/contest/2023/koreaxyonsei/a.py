# 27930
import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
  s = input()

  KOREA = 'KOREA'
  YONSEI = 'YONSEI'

  k = 0
  y = 0

  for i in s:
    if i == KOREA[k]:
       k += 1
       if k == 5:
          return KOREA
    
    if i == YONSEI[y]:
       y += 1
       if y == 6:
          return YONSEI
    
if __name__ == "__main__":
    print(solve())