text = input('Enter the Text: ')
pattern = input('Enter Pattern: ')
t = len(text)
p = len(pattern)

ans = []

for s in range(t-p+1):
    temp = s
    for i in range(p):
        if text[temp] == pattern[i]:
            temp += 1
        else:
            break
        if i == p-1:
            ans.append(s)

for i in ans:
    print('pattern found from: ',i)