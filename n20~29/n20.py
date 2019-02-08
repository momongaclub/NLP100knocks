import sys
import json
import codecs

def main():
    word2wiki = load_json(sys.argv[1])
    print(word2wiki['イギリス'])


def load_json(fname):
    word2wiki = {}
    with codecs.open(fname, 'r', 'utf-8', 'ignore') as fp:
        for line in fp:
            line = line.rstrip()
            json_data = json.loads(line)
            word2wiki[json_data['title']] = json_data['text']
    return word2wiki

if __name__ == '__main__':
    main()
