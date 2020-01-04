# fuzzy_spacy
### Combination of the FuzzyWuzzy library with Spacy PhraseMatcher

I needed a way to match phrases using a fuzzy approach to prepare an annotated dataset to train a model. After searching in forums etc., I realized that I was not the only one looking for this to work, so I share my solution here. 


## Installation

Create a virtual environment and do the following:
  
```python
git clone https://github.com/jackmen/fuzzy_spacy.git
cd /your_path/fuzzy_spacy/
pip3 install -r requirements.txt 
```

## Usage
Follow the steps presented in the jupyter notebook. 
To run the PhuzzyMatcher on a batch of documents, check the spacy documentation (https://spacy.io). 


## Comment

The code execution is not fast, but was sufficient for my use-case to annotate documents to train a NER model.  
