import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def check(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1

        if count >= 2:
            return count
    return count


def solve():
    n = int(input())
    s = input()

    for i in range(1, n):
        if check(s[:i], s[-i:]) == 1:
            return "YES"
    
    return "NO"
if __name__ == "__main__":
    print(solve())
