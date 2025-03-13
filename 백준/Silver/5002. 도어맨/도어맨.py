import sys
input = sys.stdin.readline

X = int(input())
club_line = input().strip()
stack = []
for p in club_line:
    stack.append(p)

stack = list(reversed(stack))
woman = 0
man = 0

while stack:
    cur = stack.pop()
    if cur == 'W':
        if abs((woman+1) - man) <= X:
            woman += 1
        elif stack and abs((woman+1) - man) > X:
            next = stack.pop()
            if next == 'M':
                if abs((man+1) - woman) <= X:
                    man += 1
                    stack.append(cur)
            else:
                break
        else:
            break
    else:
        if abs((man+1) - woman) <= X:
            man += 1
        elif stack and abs((man+1) - woman) > X:
            next = stack.pop()
            if next == 'W':
                if ((woman+1) - man) <= X:
                    woman += 1
                    stack.append(cur)
            else:
                break
        else:
            break
print(woman + man)