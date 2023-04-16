
import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    s = input()
    a = s.split()
    digit = 0 
    strs = 0
    gualho = 0
    for i in a:
        if i == '[':
            gualho += 8
        elif i.isdigit():
            digit += 8
        elif i == ']':
            continue
        else:
            strs += (len(i) + 12)

    print( gualho + digit + strs)

if __name__ == "__main__":
    solve()
