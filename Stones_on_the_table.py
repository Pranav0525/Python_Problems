# n stones in a row
# can be red, green or blue
# stones needed to be removed, so that no adjeaent stones are same 

n = int(input())
s = input()
count = 0
for i in range(1, n):
    if s[i-1] == s[i]:
        count += 1

print(count)