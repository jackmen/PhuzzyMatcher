from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
from scripts.utils import


class HospitalMatcher(object):
    name = "hospital_fuzzy_tagger"

    def __init__(self, nlp, label):
        self.label = label
        self.nlp = nlp

    def __call__(self, doc):
        match_list = []
        results = findfeatures(hospital_set, doc.text.lower(), match=80)
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
