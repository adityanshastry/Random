import os
import sys

from FrequencySummarizer import *


def pre_process_pdfs(pdf_dir_path, pre_processed_pdf_dir_path):

    pdf_file_text = []
    with codecs.open(os.path.join(pdf_dir_path, pdf_file_name), Constants.READ_MODE, Constants.UTF_8) as pdf_file:
        for line in pdf_file:
            pdf_file_text.append(line.lower().strip())
    pre_processed_pdf_file = codecs.open(os.path.join(pre_processed_pdf_dir_path, pdf_file_name), Constants.WRITE_MODE, Constants.UTF_8)
    for pdf_file_line in nltk.sent_tokenize(" ".join(pdf_file_text)):
        pre_processed_line = " ".join([word for word in nltk.word_tokenize(pdf_file_line) if
                                       word not in Constants.STOP_WORDS])
        pre_processed_pdf_file.write(pre_processed_line + "\n")


def main(argv):
    pre_process_pdfs(argv[1], argv[2])
    frequency_summarizer = FrequencySummarizer()
    summary = frequency_summarizer.summarize(text_path=argv[2], n=argv[3])
    print "\n".join(summary)
    pass


if __name__ == '__main__':
    main(sys.argv)
