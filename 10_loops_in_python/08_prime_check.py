num = int(input("Enter number : "))

is_prime = True

if(num > 1):
    for i in range(2,num): # Check divisibility from 2 up to num - 1 because every number is divisible by 1 and itself.
        if (num % i)  == 0 :
            is_prime = False
            break
if is_prime:
    print("it is prime ")
else :
    print("it is not prime ")
