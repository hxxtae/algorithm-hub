import sys
read = sys.stdin.readline

n,m=map(int,read().split())
count = 0
if n == 0 : print(0)
else : 
    boxes = list(map(int,read().split()))
    weight = 0
    count = 1 
    for box in boxes:   
        if box+weight <= m : 
            weight += box
        else : 
            weight = box 
            count +=1
    print(count)