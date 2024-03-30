import re
import sys
read = sys.stdin.readline

T = int(read().rstrip())

regexp = re.compile('(100+1+|01)+')
for _ in range(T):
  signal = read().rstrip()
  if regexp.fullmatch(signal):
    print("YES")
  else:
    print("NO")