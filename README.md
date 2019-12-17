# fuzzy_spacy
### Combination of the FuzzyWuzzy library with Spacy PhraseMatcher

I am a big fan of many spacy tools, but I needed a way to match phrases using a fuzzy approach to prepare a annotated dataset to train a model. All the other great rule matcher options available in spacy did not offer this flexibility. I still wanted to go on using spacy and also not lose the benefits of their framework. So with a little searching in forums etc. I realized that I was not the only one looking for this to work, so I share my solution here. 


## Usage
1. You can simply copy the functions and paste them in your pipeline
2. Clone this repo and follow the steps presented in the jupyter notebook. 

## Installation
  
Clone the repo and run setup.py 

 ```python
git clone https://github.com/jackmen/fuzzy_spacy.git
cd /your_path/fuzzy_spacy/
pip3 install -r requirements.txt 
```

## Comment

The code execution is not fast, but was sufficient for my use-case to annotate documents for model training.  
