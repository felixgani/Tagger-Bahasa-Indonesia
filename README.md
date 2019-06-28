"# Tagger Indonesia"
This is the basic API in Python Flask that uses NLP (Natural Language Processing) Spack. NLP specified in this API is used to mark POS (Talk Section) which is created using the Spacy.io library for Python. This API can be used for Indonesian, in this project there are 4 Spacy Models that can classify Indonesian with signs. Those model was built with 2 sentences corpus and 2 tagger corpus.

Sentence Corpus Source:
- Beritagar.id
- Leipzig University German

Tagger Corpus Source:
- University of Indonesia
- PAN 10

From there corpuses I made 4 models for Indonesian Tagger. Models that I made:
- Beritagar_UI
- Beritagar_PAN10
- Leipzig_UI
- Leipzig_PAN10.

Format Tagger Training with Spacy.io
[(“StatesWest melayani 10 kota di California, Arizona dan Nevada.”,{‘tags’:[‘NN’, ‘NN’, ‘CDP’, ‘NNC’, ‘IN’, ‘NN’, ‘,’, ‘NN’, ‘CC’, ‘NN’, ‘.’]})]

Tag set from Corpus University of Indonesia:
‘CC’: {‘pos’: ‘NOUN’}
‘CD’: {‘pos’: ‘CCONJ’}
‘OD’: {‘pos’: ‘NUM’}
‘DT’: {‘pos’: ‘DET’}
‘FW’: {‘pos’: ‘X’}
‘IN’: {‘pos’: ‘ADP’}
‘JJ’: {‘pos’: ‘ADJ’}
‘MD’: {‘pos’: ‘VERB’}
‘NEG’: {‘pos’: ‘NOUN’}
‘NN’: {‘pos’: ‘NOUN’}
‘NNP’: {‘pos’: ‘PROPN’}
‘NND’: {‘pos’: ‘NUM’}
‘PR’: {‘pos’: ‘PRON’}	
‘PRP’: {‘pos’: ‘PRON’}
‘RB’: {‘pos’: ‘ADV’}
‘RP’: {‘pos’: ‘PART’}
‘SC’: {‘pos’: ‘NOUN’}
‘SYM’: {‘pos’: ‘SYM’}
‘UH’: {‘pos’: ‘NOUN’}
‘VB’: {‘pos’: ‘VERB’}
‘WH’: {‘pos’: ‘PROPN’}
‘-‘: {‘pos’: ‘PUNCT’}
‘—‘: {‘pos’: ‘PUNCT’}
‘.’: {‘pos’: ‘PUNCT’}
‘:’: {‘pos’: ‘PUNCT’}
‘,’: {‘pos’: ‘PUNCT’}
‘-RRB-‘: {‘pos’: ‘PUNCT’}
‘-LRB-‘: {‘pos’: ‘PUNCT’}

Tag set from PAN10:
‘NN’: {‘pos’: ‘NOUN’}
‘VBI’: {‘pos’: ‘VERB’}
‘ADJ’: {‘pos’: ‘ADJ’}
‘FW’: {‘pos’: ‘X’}
‘IN’: {‘pos’: ‘ADP’}
‘NNP’: {‘pos’: ‘PROPN’}
‘SC’: {‘pos’: ‘NOUN’}
‘JJ’: {‘pos’: ‘ADJ’}
‘CC’: {‘pos’: ‘NOUN’}
‘RP’: {‘pos’: ‘NOUN’}
‘CDP’: {‘pos’: ‘NUM’}
‘CDO’: {‘pos’: ‘NUM’}
‘CDI’: {‘pos’: ‘NUM’}
‘CDC’: {‘pos’: ‘NUM’}
‘NEG’: {‘pos’: ‘NOUN’}
‘NNC’: {‘pos’: ‘NOUN’}
‘NNG’: {‘pos’: ‘NOUN’}
‘NNU’: {‘pos’: ‘NOUN’}
‘NNS’: {‘pos’: ‘NOUN’}
‘RB’: {‘pos’: ‘ADV’}
‘MD’: {‘pos’: ‘VERB’}
‘DT’: {‘pos’: ‘DET’}
‘UH’: {‘pos’: ‘NOUN’}
‘PRP’: {‘pos’: ‘PRON’}
‘PRN’: {‘pos’: ‘PRON’}
‘PRL’: {‘pos’: ‘PRON’}
‘SYM’: {‘pos’: ‘SYM’}
‘VB’: {‘pos’: ‘VERB’}
‘VBT’: {‘pos’: ‘VERB’}
‘WRB’: {‘pos’: ‘NOUN’}
‘WP’: {‘pos’: ‘PRON’}
‘-‘: {‘pos’: ‘SYM’}
‘—‘: {‘pos’: ‘SYM’}
‘.’: {‘pos’: ‘SYM’}
‘:’: {‘pos’: ‘SYM’}
‘,’: {‘pos’: ‘SYM’}

Those models has been evaluated, it can be concluded that the Spacy library can be used as a tool in making Indonesian tagger models that can do POS Tagging on Indonesian sentences. The use of different vector corpus does not affect the results of the Indonesian POS tagger. Indonesian Tagger Corpus with the best accuracy results with an accuracy value of 86.39% obtained from the corpus tagger PAN10 with a number of 38,531 sentences and 1,619,600 words, while the corpus tagger UI with a number of sentences of 10,030 sentences and 472,952 words obtained an accuracy of 84,73 %.

To used this API you can run:
[flask run]
  
