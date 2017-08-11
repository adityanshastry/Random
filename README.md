# Random

This repo will contain some random code written for some hackathon/fun projects:
1)  POS frequency based text summarization: This will provide the top n sentences, in any given text, which contain the highest frequency for Noun Based POS tags (NN, NNS, NNP, NNPS). </br>
    TO-DO:  Normalize the sentence frequency rank based on length of the sentence. </br>
    USAGE:  python summarize_text.py <path_to_text_file> <path_for_processed_text_file> <number_of_sentences_for_summary> </br>
    Unfortunately, the dataset this code was tried on was legislative bills introduced in the Indian Parliament. Due to extremely long sentences (as identified by NLTK), and specific language (read lawyer talk), this method didnt perform as well. The hope is that this can be used as a baseline for some generic dataset.

Libraries used:
1) NLTK:  To perform sentence/word tokenization, and get the POS tags on the sentences
