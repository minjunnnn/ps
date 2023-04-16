import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

def solve():
    q = int(input())
    currSmallest = 1
    added = []

    for i in range(q):
        a = input()

        if a[0] == '0':
            if added:
                if added[-1][0] == 'a':
                    a_ = int(added[-1][2:]) + int(a[2:])
                    added[-1] = f'a {a_}'
                else:
                    a_ = int(a[2:])
                    added.append(f'a {a_}')
            else:
                a_ = int(a[2:])
                added.append(f'a {a_}')
        elif a[0] == '1':
            if added:
                if added[-1][0] == 'm':
                    a_ = int(added[-1][2:]) * int(a[2:])
                    added[-1] = f'm {a_}'
                else:
                    a_ = int(a[2:])
                    added.append(f'm {a_}')
            else:
                a_ = int(a[2:])
                added.append(f'm {a_}')
        elif a[0] == '2':
            currSmallest += int(a[2:])
        else:
            curr = currSmallest
            for i in added:
                c, command = i.split()

                if c == 'a':
                    curr += int(command)
                else:
                    curr *= int(command)
            print(curr)
                    
    

if __name__ == "__main__":
    solve()
