line = input().split()
k = int(line[0])
n = int(line[1])
w = int(line[2])
total_money = 0
for i in range(1, w+1):
    total_money += i*k

if total_money <= n:
    print(0)
else:
    print(total_money - n)