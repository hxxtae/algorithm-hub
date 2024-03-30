import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split(' '))
NO_LISTEN = [read().rstrip() for _ in range(N)]
NO_SEE = [read().rstrip() for _ in range(M)]

noListenSee = sorted(set(NO_LISTEN) & set(NO_SEE))
print(len(noListenSee))
print("\n".join(noListenSee))