import re
import nltk
import heapq
from gensim.summarization.summarizer import summarize

def summa(para):
    text = ""
    for line in para:
        text = text + line.text

    # print(text)
    # print("\n")

    text = re.sub(r'Also Read', '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'-', ' - ', text)
    text = re.sub(r'Y.S.', 'Y S', text)
    clean_text = text.lower()
    # print(clean_text)
    # print("\n")
    stopwords = nltk.corpus.stopwords.words('english')
    stopwords = stopwords + [',', '(', ')', '“', '”', '.', '-', ':', '’', '~', '!', '`', '@', '#', '$', '%', '&', '*',
                             '+', '/', ';', '<', '>', '?', '[', ']', '{', '}', '_']
    # len(stopwords)
    # print(stopwords)
    # print("\n")
    sentence_list = nltk.sent_tokenize(text)
    # len(sentence_list)
    # print(sentence_list)
    # print("\n")
    word_list = clean_text.split()
    # print(word_list)
    # print("\n")
    word_frequencies = {}

    for word in nltk.word_tokenize(clean_text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    # print(word_frequencies)
    # print("\n")
    max_frequency = max(word_frequencies.values())
    # print(max_frequency)
    # print("\n")
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word] / max_frequency)

    # print(word_frequencies)
    # print("\n")
    # sorted(word_frequencies.values(), reverse=True)
    weight_words = sorted(word_frequencies.items(), reverse=True, key=lambda x: x[1])

    # for ele in weight_words :
    # print(ele[0] , " : " , ele[1] )

    sentence_score = {}

    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if word not in [",", "."]:
                    # print(word)
                    # if len(sent.split(' ')) < 50:
                    if sent not in sentence_score.keys():
                        sentence_score[sent] = word_frequencies[word]
                    else:
                        sentence_score[sent] += word_frequencies[word]

    # print("\n")
    # print(sentence_score)
    # print("\n")
    # print(len(sentence_score))
    # print("\n")
    if len(sentence_score) <= 10:
        summary_sentences = heapq.nlargest(5, sentence_score, key=sentence_score.get)
    elif (len(sentence_score) > 10 and len(sentence_score) <= 15):
        summary_sentences = heapq.nlargest(9, sentence_score, key=sentence_score.get)
    else:
        summary_sentences = heapq.nlargest(11, sentence_score, key=sentence_score.get)
    summary = ' '.join(summary_sentences)
    # print(summary)
    return summary


def gensima(para):
    text = ""
    for line in para:
        text = text + line.text
    text = re.sub(r'Also Read', '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'-', ' - ', text)
    text = re.sub(r'\[[0-9]*\]',' ',text)
    geni = summarize(text,ratio=0.5)
    return geni