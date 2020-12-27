from decimal import Decimal
li={}
for _ in range(int(input())):
    name, *line = input().split()
    scores = list(map(float, line))
    li[name] = scores
    # print(li)
    # print(type(li))
    # name, *line = input().split()

qName = input()
total = sum(li[qName])
avg = Decimal(total/3)
print(round(avg))