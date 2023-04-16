
import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def check(arr):
    global n, B
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                if B[i][j] == 0:
                    return False

    return True

def rotate90(arr):
    global n
    arr_ = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            arr_[i][j] = arr[n-1-j][i]
    
    return arr_



def solve():
    global n, B
    n = int(input())
    A = [[*map(int, input().split())] for i in range(n)]
    B = [[*map(int, input().split())] for i in range(n)]

    for i in range(4):
        A = rotate90(A)
        if check(A):
            return "Yes"

    return "No"

if __name__ == "__main__":
    print(solve())
