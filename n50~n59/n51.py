import sys

def load_words(text):
    words = []
    with open(text, 'r') as fp:
        for line in fp:
            line = line.rstrip()
            line = line.split(' ')
            for word in line:
                words.append(word)
    return words

def main():
    en_words = load_words(sys.argv[1])
    for en_word in en_words:
        print(en_word)

if __name__ == '__main__':
    main()
