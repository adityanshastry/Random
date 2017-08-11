import codecs
from collections import defaultdict
from heapq import nlargest

import nltk

import Constants


class FrequencySummarizer:
    def __init__(self):
        """
            Initilize the text summarizer.
            Words that have a frequency term lower than min_cut
            or higer than max_cut will be ignored.
        """
        self.words_from_pos_tags = {}

        for pos_tag in Constants.NOUN_POS_TAGS:
            self.words_from_pos_tags[pos_tag] = defaultdict(int)

        pass

    def _compute_frequencies(self, sentences):
        """
          Compute the frequency of each of word.
          Input:
           word_sent, a list of sentences already tokenized.
          Output:
           freq, a dictionary where freq[w] is the frequency of w.
        """
        for sentence in sentences:
            for (word, pos_tag) in nltk.pos_tag(nltk.word_tokenize(sentence)):
                if pos_tag in Constants.NOUN_POS_TAGS:
                    self.words_from_pos_tags[pos_tag][word] += 1

        for pos_tag in self.words_from_pos_tags:
            if len(self.words_from_pos_tags[pos_tag].values()) > 0:
                normalizer = float(max(self.words_from_pos_tags[pos_tag].values()))
                for word in self.words_from_pos_tags[pos_tag].keys():
                    self.words_from_pos_tags[pos_tag][word] /= normalizer

    def summarize(self, text_path, n):
        """
          Return a list of n sentences
          which represent the summary of text.
        """
        sentences = codecs.open(text_path, Constants.READ_MODE, Constants.UTF_8).readlines()
        assert n <= len(sentences)
        self._compute_frequencies(sentences)
        ranking = defaultdict(int)

        for i, sentence in enumerate(sentences):
            for (word, pos_tag) in nltk.pos_tag(nltk.word_tokenize(sentence)):
                if pos_tag in Constants.NOUN_POS_TAGS:
                    ranking[i] += self.words_from_pos_tags[pos_tag][word]
        sents_idx = self._rank(ranking, n)
        return [sentences[j] for j in sents_idx]

    def _rank(self, ranking, n):
        """ return the first n sentences with highest ranking """
        return nlargest(n, ranking, key=ranking.get)
