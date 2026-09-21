def even_num(limit):
    for i in range(2,limit+1,2): # 2 means in last 1 num skip from 2 so 3 skip 4 5 skip 6
        yield i

for n in even_num(10):
    print(n)
