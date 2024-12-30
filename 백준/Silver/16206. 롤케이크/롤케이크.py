import sys
read = sys.stdin.readline

N,M=map(int,read().split())

roll_cake=list(map(int,read().split()))
roll_cake=sorted(roll_cake)
roll_cake=sorted(roll_cake, key=lambda x:x%10)

count=0

for cutting in roll_cake:
    if M>0:
        if cutting<10:
            continue
        elif cutting%10==0:
            temp=(cutting//10)-1
            if temp==0:
                count+=1
            else:
                if(M>=temp):
                    count+=temp+1
                    M-=temp
                else:
                    count+=M
                    break
        else:
            temp=(cutting//10)
            if (M>=temp):
                count+=temp
                M-=temp
            else:
                count+=M
                break
    else:
        break

print(count)