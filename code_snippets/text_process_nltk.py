import nltk
from nltk.stem import WordNetLemmatizer
stopwords = nltk.download('stopwords')


def my_tokenizer(s):
    # split string into words (tokens)
    tokens = nltk.tokenize.word_tokenize(s.lower())

    tokens = [t for t in tokens if len(t) > 2] # remove short words
    tokens = [WordNetLemmatizer.lemmatize(t) for t in tokens] # base form
    tokens = [t for t in tokens if t not in stopwords.words()] # remove stopwords
    tokens = [t for t in tokens if not any(c.isdigit() for c in t)]
    return tokens



def tokens_gen(tokens):
    for t in tokens:
        if len(t) > 2:
            t = WordNetLemmatizer.lemmatize(t)
            if t not in stopwords.words():
                for c in t:
                    if not any(c.isdigit()):
                        yield t


def my_tokenizer_2(s):
    # split string into words (tokens)
    tokens = nltk.tokenize.word_tokenize(s.lower())
    return tokens_gen(tokens)
