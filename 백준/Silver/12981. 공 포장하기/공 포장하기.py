from sys import stdin
R, G, B = map(int,stdin.readline().split())

MIN = min(R,G,B)
result = MIN
R -= MIN
G -= MIN
B -= MIN

result += R//3 + G//3 + B//3
R %= 3
G %= 3
B %= 3

if R == 2:
  result += 1
  R = 0
if G == 2:
  result += 1
  G = 0
if B == 2:
  result += 1
  B = 0

if R+G+B > 0:
  result += 1
print(result)