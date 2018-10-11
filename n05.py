def seq2ngram(seq, n):
    seq_list = seq.split()
    word_bigram = [seq_list[i:i+n] for i in range(len(seq_list) - n + 1)]
    str_bigram = [seq[i:i+n] for i in range(len(seq) - n + 1)]
    print(word_bigram, str_bigram)


seq2ngram("I am an NLPer", 2)
