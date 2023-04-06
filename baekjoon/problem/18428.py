#18428
import sys
input = lambda: sys.stdin.readline().rstrip()

dx = (-1, 0, 1, 0)
dy = (0, 1, 0 , -1)

def check():
   global graph, teacher, n
   for tx, ty in teacher:
      for d in range(4):
        dir = 1
        while True:
           nx = tx + dx[d] * dir
           ny = ty + dy[d] * dir

           if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == 'O':
              break
           
           if graph[nx][ny] == 'S':
              return False
           
           dir += 1
  
   return True


def solve():
  global graph, teacher, n
  n = int(input())
  graph = [input().split() for i in range(n)]

  teacher = []
  empty = []

  for i in range(n):
     for j in range(n):
        if graph[i][j] == 'T':
           teacher.append((i, j))
        elif graph[i][j] == 'X':
           empty.append((i, j))
  
  
  es = len(empty)
  for i in range(es):
     for j in range(i+1, es):
        for z in range(j+1, es):
           graph[empty[i][0]][empty[i][1]] = 'O'
           graph[empty[j][0]][empty[j][1]] = 'O'
           graph[empty[z][0]][empty[z][1]] = 'O'
           if check():
              return "YES"
           graph[empty[i][0]][empty[i][1]] = 'X'
           graph[empty[j][0]][empty[j][1]] = 'X'
           graph[empty[z][0]][empty[z][1]] = 'X'
        
  return "NO"

    
if __name__ == "__main__":
    print(solve())