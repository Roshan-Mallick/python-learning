def sum_all(*args):  # *args allows multiple parameters to be passed
    #print(*args)
    #print(args)  # The arguments are stored as a tuple

    sum = 0
    for i in args:
        print(i)
        sum += i

    print("sum of above : ",sum)

sum_all(1, 2, 3, 4)
