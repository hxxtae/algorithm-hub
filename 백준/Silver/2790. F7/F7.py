import sys
read = sys.stdin.readline

t = int(read().rstrip())
my_list = []
for i in range(t) :
    my_list.append(int(read().rstrip()))
my_list = sorted(my_list)
for i in range(len(my_list)) :
    my_list[i] = my_list[i] + t
    t -=1
my_cnt = 0
max_v = max(my_list)
for i in range(len(my_list)-1) :
    if my_list[i] >= max_v :
        my_cnt +=1
    t += 1
    my_list[i+1] += t

if my_list[-1] > max_v :
    print(my_cnt+1)
else :
    print(my_cnt)