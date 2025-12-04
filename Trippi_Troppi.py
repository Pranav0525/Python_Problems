T = int(input())
ans = []
for _ in range(T):
    sen = input().split()
    abb_name = sen[0][0] + sen[1][0] + sen[2][0]
    ans.append(abb_name)

print("\n".join(ans))