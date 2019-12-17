import nltk
from nltk.corpus import stopwords
import re
from fuzzywuzzy import fuzz
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
stop_words.add(".")
stop_words.add(",")
stop_words.add("!")
stop_words.add("(")
stop_words.add(")")


def fuzzy_matcher(features, document, match=None):
    matches = []
    for feature in features:
        feature_length = len(feature.split(" "))
        tokens = nltk.word_tokenize(document)
        for i in range(len(tokens) - feature_length + 1):
            matched_phrase = ""
            j = 0
            for j in range(i, i + feature_length):
                if re.search(r'[,!?{}\[\]]', tokens[j]):
                    break
                matched_phrase = matched_phrase + " " + tokens[j].lower()
            matched_phrase.strip()
            if not matched_phrase == "":
                if fuzz.ratio(matched_phrase, feature.lower()) > match:
                    matches.append([matched_phrase, feature, i, j])
    return matches


def fuzzy_matcher_stopwords(features, document, match=None):
    matches = []
    for feature in features:
        feature_length = len(feature.split(" "))
        tokens = nltk.word_tokenize(document)
        tokens_no_stop = [w for w in tokens not in stop_words]
        for i in range(len(tokens_no_stop) - feature_length + 1):
            matched_phrase = ""
            j = 0
            for j in range(i, i + feature_length):
                if re.search(r'[,!?{}\[\]]', tokens_no_stop[j]):
                    break
                matched_phrase = matched_phrase + " " + tokens_no_stop[j].lower()
            matched_phrase.strip()
            if not matched_phrase == "":
                if fuzz.ratio(matched_phrase, feature.lower()) > match:
                    matches.append([matched_phrase, feature, i, j])
    return matches
