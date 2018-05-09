str = "stresed"
reverse = ""
for i in range(0, len(str)):
    reverse += str[len(str)-1-i]
print(reverse)

reverse = str[::-1]
print(reverse)
