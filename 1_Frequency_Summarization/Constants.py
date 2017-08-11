from nltk.corpus import stopwords
from string import punctuation

NOUN_POS_TAGS = ("NN", "NNP", "NNPS", "NNS")
STOP_WORDS = set(stopwords.words('english'))
PUNCTUATIONS = set(unicode(punctuation))
READ_MODE = "r"
WRITE_MODE = "w"
UTF_8 = "utf-8-sig"
