# import os, io, sys
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
import sys
print = sys.stdout.write
# import time
# from pprint import pprint
input = lambda: sys.stdin.readline().rstrip()
max_ = -sys.maxsize
def rotate90(arr):
  global n
  arr_ = [[0 for i in range(4)] for i in range(4)]
  for i in range(4):
    for j in range(4):
      arr_[j][3-i] = arr[i][j]
  return arr_


def check(g):
  global max_
  sum_ = 0
  for i in range(5):
    for j in range(5):
      curr = g[i*5+j]
      color = curr[0]
      cost = curr[1]

      if color == 'R':
        sum_ += int(cost) * 7
      elif color == 'B':
        sum_ += int(cost) * 5
      elif color == 'G':
        sum_ += int(cost) * 3
      elif color == 'Y':
        sum_ += int(cost) * 2
      else:
        pass
  max_ = max(max_, sum_)
  # print(max_)
  return
    



def backtracking(g, count, s):
  global materials, n
  if count == 3:
    check(g)
    return
  
  for i in range(n):
    if i in s:
      continue
    for moveX in range(2):
      for moveY in range(2):
        for r in range(4):
          k = [*g]
          for x in range(4):
            for y in range(4):
              c = (x + moveX) * 5 + (y + moveY)
              currColor = k[c][0]
              currCost = int(k[c][1])
              addedColor = materials[i][r][x][y][1]
              addedCost = int(materials[i][r][x][y][0])

              nextCost = currCost+ addedCost
              
              if nextCost < 0:
                nextCost = 0
              elif nextCost >= 10:
                nextCost = 9 
              else:
                pass
              
              if addedColor == 'W':
                nextColor = currColor
              else:
                nextColor = addedColor
              
              k[c] = nextColor + str(nextCost)
          s.add(i)
          backtracking(k, count+1, s)
          s.remove(i)

def solve():
  global materials, n
  n = int(input())
  materials = [[[[[0, 0] for i in range(4)] for i in range(4)]for i in range(4)]for i in range(n)]

  for i in range(n):
    for j in range(2):
      for x in range(4):
         stats = input().split()
         for y in range(4):
           materials[i][0][x][y][j] = stats[y]
  
  for i in range(n):
    for r in range(1, 4):
      materials[i][r] = rotate90(materials[i][r-1])
  s = set()
  graph = ['W0' for i in range(25)]
  for i in range(n):
    for moveX in range(2):
      for moveY in range(2):
        k = [*graph]
        for x in range(4):
          for y in range(4):
            c = (x + moveX) * 5 + (y + moveY)
            currColor = k[c][0]
            currCost = int(k[c][1])
            addedColor = materials[i][0][x][y][1]
            addedCost = int(materials[i][0][x][y][0])

            nextCost = currCost+ addedCost
              
            if nextCost < 0:
              nextCost = 0
            elif nextCost >= 10:
              nextCost = 9 
            else:
              pass
              
            if addedColor == 'W':
              nextColor = currColor
            else:
              nextColor = addedColor
              
            k[c] = nextColor + str(nextCost) 
        s.add(i)        
        backtracking(k, 1, s)
        s.remove(i)

if __name__ == "__main__":
  # start = time.time()
  solve()
  # end = time.time()

  # print(f"{end - start:.5f} sec")
  print(str(max_))
