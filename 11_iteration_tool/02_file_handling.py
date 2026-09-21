f = open('/home/eth0x1/Desktop/python-learning/11_iteration_tool/test.py')

while True:
    line = f.readline()

    if not line:
        break

    print(line, end=" ")

check = iter(f) is f
print(check)
print(type(check))

f.close()
