import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    n = int(input())
    board = [[*map(int, input().split())] for i in range(n)]
    loc = [n // 2 - 1, n // 2, n // 2 - 1, n // 2]
    count = 0
    k = ''

    while True:
        a = [[0, i] for i in range(4)]

        if loc[2] - 1 >= 0:
            s = loc[0] if loc[0] >= 0 else 0 
            e = loc[1]+1 if loc[1]+1 <= n else n 
            for i in range(loc[0], loc[1] + 1):
                a[0][0] += board[loc[2] - 1][i]

        if loc[3] + 1 < n:
            s = loc[0] if loc[0] >= 0 else 0 
            e = loc[1]+1 if loc[1]+1 <= n else n 
            for i in range(loc[0], loc[1] + 1):
                a[1][0] += board[loc[3] + 1][i]

        if loc[0] - 1 >= 0:
            s = loc[2] if loc[2] >= 0 else 0 
            e = loc[3]+1 if loc[3]+1 <= n else n 
            for i in range(loc[2], loc[3] + 1):
                a[2][0] += board[i][loc[0] - 1]

        if loc[1] + 1 < n:
            s = loc[2] if loc[2] >= 0 else 0 
            e = loc[3]+1 if loc[3]+1 <= n else n 
            for i in range(loc[2], loc[3] + 1):
                a[3][0] += board[i][loc[1] + 1]

        maxA = max(a, key=lambda x: (x[0], -x[1]))
        if maxA[0] <= 0:
            break
        else:
            if maxA[1] == 0:
                loc[2] -= 1
                k += 'U'
            elif maxA[1] == 1:
                loc[3] += 1
                k += 'D'
            elif maxA[1] == 2:
                loc[0] -= 1
                k += 'L'
            else:
                loc[1] += 1
                k += 'R'
            count += maxA[0]
    output(f"{count}\n{k}\n")

if __name__ == "__main__":
    solve()
