import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = list(map(int, read().rstrip().split()))

def confirmSurvive(arr):
  A = arr[0]
  for Ai in sorted(arr[1:N], key=lambda x: x):
    if A > Ai: 
      A += Ai
    else: 
      return "No"
    
  return "Yes"

print(confirmSurvive(ARR))