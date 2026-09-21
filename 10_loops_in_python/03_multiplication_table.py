num = int(input("Enter number : "))

for i in range(1,10+1):
    if (i == 5) :
        continue
    ans = num * i
    print(num,"x",i,"=",ans)
