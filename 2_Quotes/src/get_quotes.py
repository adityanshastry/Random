from bs4 import BeautifulSoup
import urllib2
import codecs
import Constants


def get_and_save_quotes(author):
    quotes_file = codecs.open("../data/quotes.txt", "w", encoding="utf8")
    base_url = "https://www.goodreads.com/author/quotes/{}?page={}"
    for page_num in xrange(1, Constants.authors[author]["max_pages"] + 1):
        print base_url.format(Constants.authors[author]["url_component"], str(page_num))
        soup = BeautifulSoup(
            urllib2.urlopen(base_url.format(Constants.authors[author]["url_component"], str(page_num))).read())
        for quote in soup.find_all("div", {'class': 'quoteText'}):
            if quote:
                # print quote.text.strip()
                quotes_file.write(quote.text.strip() + "\n")

    quotes_file.close()


def main():
    get_and_save_quotes("george_carlin")


if __name__ == '__main__':
    main()
