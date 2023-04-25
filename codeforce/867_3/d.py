import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    n = int(input())
    s = 0
    L = [n]
    visited = [False] * (n + 1)
    visited[n] = True
    flag = True
    for i in range(n-1,0,-1):
        curr = s
        if flag:
            s += i
        else:
            s -= i

        if curr > s:
            k = n + s
            kk = k - curr
        else:
            kk = s - curr

        if visited[kk]:
            return [-1]
        else:
            visited[kk] = True
            flag = True if not flag else False

        L.append(kk)

    return L

        


        




        


if __name__ == "__main__":
    for i in range(int(input())):
        print(*solve())
