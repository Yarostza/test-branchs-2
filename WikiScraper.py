import wikipedia
import re
import pickle
from datetime import datetime


def get_page_text(article_name):
    # the following code was learned from:
    # https://levelup.gitconnected.com/two-simple-ways-to-scrape-text-from-wikipedia-in-python-9ce07426579b

    try:
        # Specify the title of the Wikipedia page
        wiki_page = wikipedia.page(article_name)
        # Extract the plain text content of the page
        page_text = wiki_page.content
        # Clean up the text
        page_text = re.sub(r'==.*?==+', '', page_text)
        page_text = page_text.replace('\n', '')
        return page_text
    except:
        return False


def wiki_scrape(article_name, get_connected_article_text):
    title_text_dict = dict()
    list_of_article_names = list()
    list_of_article_names.append(article_name)
    if get_connected_article_text:
        list_of_article_names = list_of_article_names + wikipedia.page(article_name).links
        # print(list_of_article_names)
    for article in list_of_article_names:
        text = get_page_text(article)
        if text:
            print("adding text from: ", article)
            title_text_dict[article] = text
        else:
            print("FAILED. Exact title did not exist for: ", article)
    send_to_pickle(title_text_dict)


def send_to_pickle(title_text_dict):
    # used the following link as an example:
    # https://www.geeksforgeeks.org/understanding-python-pickling-example/

    now = datetime.now()
    now_string = now.strftime("%m-%d-%Y_%H:%M:%S")
    file_name = "title_text_dict_" + now_string
    text_dict_file = open(file_name, 'ab')
    pickle.dump(title_text_dict, text_dict_file)
    text_dict_file.close()
    print("saved to pickle: ", file_name)


def load_data(file_name):
    # this function is based on:
    # https://www.geeksforgeeks.org/understanding-python-pickling-example/

    pickled_file = open(file_name, 'rb')
    loaded_title_text_dict = pickle.load(pickled_file)
    pickled_file.close()
    print(loaded_title_text_dict)


if __name__ == '__main__':
    # takes in title of wikipedia article you want the text from, and bool.
    # True if you also want text from every linked article.
    wiki_scrape('pycharm', True)
    # load_data("title_text_dict_12-10-2021_17:04:38")
