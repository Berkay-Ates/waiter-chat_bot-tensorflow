import string
import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np

# nltk.download("punkt")


def tokenize(sentence):
    return nltk.word_tokenize(sentence)


def stem(word: string):
    stemmer = PorterStemmer()
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0

    return bag


sentence = ["hello", "how", "are", "you"]
words = ["hello", "hi", "i", "you", "by", "thank", "cool"]
bag = bag_of_words(sentence, words)
print(bag)

# a = "How long does shipping take?"
# print(a)

# a = tokenize(a)
# print(a)

# for w in a:
#     print(stem(w))


# words = ["organize", "organizes", "organizing"]
# stemmed_words = [stem(word) for word in words]
# print(stemmed_words)
