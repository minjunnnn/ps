
import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def rotate90(arr):  
  global n
  arr_ = [[0 for i in range(n)] for i in range(n)]
  for i in range(n):
    for j in range(n):
      arr_[j][n-1-i] = arr[i][j]
  return arr_

def oper2048(board, operIndex):
    global n
    result = [] 
    maxx = -sys.maxsize
    flag = True
    if operIndex == 0:
        for i in range(n):
            tmp = []
            for j in range(n):
                if board[i][j] != 0:
                    tmp.append(board[i][j])
            currX = 0
            container = []
            while currX + 1 < len(tmp):
                if(tmp[currX] == tmp[currX+1]):
                    container.append(tmp[currX] * 2)
                    maxx = max(tmp[currX] * 2, maxx)
                    currX += 2
                else:
                    container.append(tmp[currX])
                    maxx = max(tmp[currX], maxx)
                    currX += 1
            if currX == len(tmp) - 1:
                container.append(tmp[currX])
            if n - len(container) != 0:
                flag = False
            for i in range(n - len(container)):
                container.append(0)
            result.append(container)  
    elif operIndex == 1:
        for i in range(n):
            tmp = []
            for j in range(n):
                if board[i][j] != 0:
                    tmp.append(board[i][j])
            currX = len(tmp)-1
            container = []
            while currX - 1 > -1:
                if(tmp[currX] == tmp[currX-1]):
                    container.append(tmp[currX] * 2)
                    maxx = max(tmp[currX] * 2, maxx)
                    currX -= 2
                else:
                    container.append(tmp[currX])
                    maxx = max(tmp[currX], maxx)
                    currX -= 1
            if currX == 0:
                container.append(tmp[currX])

            if n - len(container) != 0:
                flag = False
            for i in range(n - len(container)):
                container.append(0)

            result.append([*reversed(container)])

    elif operIndex == 2:
        for j in range(n):
            tmp = []
            for i in range(n):
                if board[i][j] != 0:
                    tmp.append(board[i][j])
            currX = 0
            container = []
            while currX + 1 < len(tmp):
                if(tmp[currX] == tmp[currX+1]):
                    container.append(tmp[currX] * 2)
                    maxx = max(tmp[currX] * 2, maxx)
                    currX += 2
                else:
                    container.append(tmp[currX])
                    maxx = max(tmp[currX] , maxx)
                    currX += 1
            if currX == len(tmp) - 1:
                container.append(tmp[currX])
            
            if n - len(container) != 0:
                flag = False
            for i in range(n - len(container)):
                container.append(0)
            result.append(container)
        result = [*map(list,[*zip(*result)])]
#        result = rotate90(result)
    else:
        for j in range(n):
            tmp = []
            for i in range(n):
                if board[i][j] != 0:
                    tmp.append(board[i][j])
            currX = len(tmp)-1
            container = []
            while currX - 1 > -1:
                if(tmp[currX] == tmp[currX-1]):
                    container.append(tmp[currX] * 2)
                    maxx = max(tmp[currX] * 2, maxx)
                    currX -= 2
                else:
                    container.append(tmp[currX])
                    maxx = max(tmp[currX], maxx)
                    currX -= 1

            if currX == 0:
                container.append(tmp[currX])
            if n - len(container) != 0:
                flag = False
            for i in range(n - len(container)):
                container.append(0)
            result.append([*reversed(container)])

        result_ = [[0 for i in range(n)] for _ in range(n)]
        for ii in range(n):
            for jj in range(n):
                result_[jj][ii] = result[ii][jj]
        result = result_
        
    return (result, maxx, flag)

def checkmax(arr):
    global n
    max_ = -sys.maxsize
    for i in range(n):
        max_ = max(max_, max(arr[i]))
    return max_


def backtracking(board, count, maxValue):
    global n, m_
    #print(*board, sep="\n")
    #print(count)
    if count == 5:
        c = checkmax(board)
        m_ = max(m_, c)
        return 
    if maxValue * (2 ** (10 - count)) < m_:
        return 
    for i in range(4):
        #board_ = [j[:] for j in board]
        b_, maxx, f = oper2048(board_, i)
        m_ = max(maxx, m_) 
        if f:
            continue
        backtracking(b_, count+1, maxx)

def solve():
    global n, m_
    m_= -sys.maxsize
    n = int(input())
    board = [[*map(int ,input().split())] for i in range(n)]
    m_ = max(m_, checkmax(board))
    for i in range(4):
        #board_ = [j[:] for j in board]
        b_, maxx, f = oper2048(board_, i)
        m_ = max(maxx, m_)
        if f:
            continue
        backtracking(b_, 1, maxx)
        #print(*oper2048(board_, i), sep="\n")
        #print()

if __name__ == "__main__":
    solve()
    output(str(m_))
