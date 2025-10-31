n = int(input())
for _ in range(n):
    is_square = list(map(int, input().split()))
    if len(set(is_square)) == 1:
        print("Yes")
    else:
        print("No")