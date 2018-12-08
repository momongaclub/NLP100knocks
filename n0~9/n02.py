word1 = 'パトカー'
word2 = 'タクシー'
answer = ''

for w1, w2 in zip(word1, word2):
    answer += w1 + w2

print(answer)
