n = list(map(int, input().split()))
r = int(input())
c = int(input())
print("Reshaped Array:")
reshaped_array = []
index = 0
for i in range(r):
    new_row = []
    for j in range(c):
        new_row.append(n[index])
        index += 1
    reshaped_array.append(new_row)
print(reshaped_array)