import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    n = int(input())
    s = input()
    gFlag = False
    xFlag = False

    for i in s:
        if i == 'x':
            xFlag = True
        elif i == 'o':
            gFlag = True
        else:
            pass

    if gFlag and not xFlag:
        print("Yes")
    else:
        print("No")



if __name__ == "__main__":
    solve()
