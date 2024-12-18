import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = list(map(int, read().rstrip().split()))

def solution(n, chains):
  count = 0
  chains.sort()
  use_chain = 0
  for chain in chains:
    if chain == n - 1:
      return use_chain + chain
    elif chain > n - 1:
      return use_chain + n - 1
    else:
      n -= (chain + 1)
      use_chain += chain
    
  return count

print(solution(N, ARR))