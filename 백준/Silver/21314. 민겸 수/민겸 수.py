import sys
 
w = sys.stdin.readline().strip()
Max = Min = ""
m = 0
for i in range(len(w)):
    if w[i] == "M":
        m += 1
    elif w[i] == "K":
        if m:
            Min += str(10 ** m + 5)
            Max += str(5 * (10 ** m ))
        else:
            Min += "5"
            Max += "5"
        m = 0
if m:
    Min += str(10 ** (m - 1))
    while m:
        Max += "1"
        m -= 1
print(Max)
print(Min)