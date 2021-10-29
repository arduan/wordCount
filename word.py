# Подсчет частоты слов в произведении Пушкина Метель.
import string
import nltk
import time
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from wordcloud import WordCloud
from pylab import figure, axes, pie, title, show
import matplotlib.pyplot as plt

f = open("pushkin-metel.txt", "r", encoding="utf-8")

# очистка
text = f.read()
text = text.lower()
spec_chars = string.punctuation + "\n\xa0«»\t--..."

def remove_chars_from_text(text, chars):
    return "".join([ch for ch in text if ch not in chars])

text = remove_chars_from_text(text, spec_chars)     #уд. спецсимволов
text = remove_chars_from_text(text, string.digits)  #уд. цифры

# создаем токены
nltk.download("punkt")            #подключаем punkt
text_tokens = word_tokenize(text) #получаем токены

# очистка, стоп слова
nltk.download("stopwords")
russian_stopwords = stopwords.words("russian")
text_tokens = [token.strip() for token in text_tokens if token not in russian_stopwords] #токены списком без стоп слов

text = nltk.Text(text_tokens) # меняем тип для работы с методами nltk
fdist = FreqDist(text)

print(fdist.most_common(5)) # топ 5 по частотности слов