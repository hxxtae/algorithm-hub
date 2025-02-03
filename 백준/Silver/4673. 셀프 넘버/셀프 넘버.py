n_lst = set(range(1, 10001))
rmv_lst = set()

for i in n_lst :
    for j in str(i) :
        i += int(j)
    rmv_lst.add(i)

self_numbers = n_lst - rmv_lst
for s in sorted(self_numbers) :
    print(s)