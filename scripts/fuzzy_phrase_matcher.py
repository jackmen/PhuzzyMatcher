import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

nlp = spacy.blank('en')


class PhuzzyMatcher(object):
    name = "phuzzy_matcher"

    def __init__(self, nlp, set, fuzzy_matcher, match, label, stop_words = None):
        self.nlp = nlp
        self.set = set
        self.fuzzy_matcher = fuzzy_matcher
        self.fuzzy_matcher_stopwords = fuzzy_matcher
        self.match = match
        self.label = label
        self.stop_words = stop_words

    def __call__(self, doc):
        match_list = []
        if self.stop_words:
            results = self.fuzzy_matcher_stopwords(self.set, doc.text.lower(), self.match, self.stop_words)
        else:
            results = self.fuzzy_matcher(self.set, doc.text.lower(), self.match)
        for i in results:
            match_list.append(str(i[0].lstrip()))
        patterns = [nlp.make_doc(text) for text in match_list]  # noqa: F821
        matcher = PhraseMatcher(self.nlp.vocab, attr='LOWER')
        matcher.add(self.label, None, *patterns)
        matches = matcher(doc)
        seen_tokens = set()
        new_entities = []
        entities = doc.ents
        for match_id, start, end in matches:
            if start not in seen_tokens and end - 1 not in seen_tokens:
                new_entities.append(Span(doc, start, end, label=match_id))
                entities = [
                    e for e in entities if not (e.start < end and e.end > start)
                ]
                seen_tokens.update(range(start, end))

        doc.ents = tuple(entities) + tuple(new_entities)
        return doc
