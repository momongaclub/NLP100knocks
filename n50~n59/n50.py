import sys
import re

PATTERN = '[.;:?!]\s[A-Z]'

def load_text(text):
    lines = []
    with open(text, 'r') as fp:
        for line in fp:
            line = line.rstrip()
            line = re.split(PATTERN, line)
            lines.append(line)
    return lines

def main():
    en_texts = load_text(sys.argv[1])
    for en_text in en_texts:
        print(en_text)

if __name__ == '__main__':
    main()
