"""
Problem Statement:

For every word in the file,
Add to the dictionary if it doesn't exist.
If it does, increase the count.

Hint: To eliminate duplicates, remember to split by punctuation,
And use case demiliters. The functions lower() and split() will be useful!
"""
import collections


def get_stop_words(stopwords_filename="stopwords"):
    with open(stopwords_filename) as stpFin:
        stopwords = set(line.strip() for line in stpFin.readlines())
    return stopwords


def count_stopwords(stopwords, filename="98-0.txt"):
    """
    :param stopwords:
    :param filename:
    :return:
    """

    wordcount = {}
    with open(filename) as fin:
        for word in fin.read().lower().split():
            word = word.replace(".", "")
            word = word.replace(",", "")
            word = word.replace("\"", "")
            word = word.replace("“", "")
            if word not in stopwords:
                wordcount[word] = wordcount.get(word, 0) + 1

    d1 = collections.Counter(wordcount)
    for word, count in d1.most_common(10):
        print(word, ": ", count)


def main():
    stopwords = get_stop_words()
    count_stopwords(stopwords)


if __name__ == "__main__":
    main()
