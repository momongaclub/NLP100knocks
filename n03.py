string = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

answer = []
#正規表現で文字列しかとれないようにする
string = string.replace(',','')
string = string.replace('.','')

words = string.split()

for word in words:
    answer.append(len(word))

print(answer)
