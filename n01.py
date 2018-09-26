string = 'パタトクカシーー'
answer = ''
for i in range(0, len(string)):
    if i % 2 == 0:
        answer += string[i]

print(answer)
