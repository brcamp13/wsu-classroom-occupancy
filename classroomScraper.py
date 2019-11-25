from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def get_all_html_content_from_url(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    Taken from: https://realpython.com/python-web-scraping-practical-introduction/
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response appears to be HTML, false otherwise
    Taken from: https://realpython.com/python-web-scraping-practical-introduction/
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

def log_error(e):
    """
    Logs errors by simply printing them 
    Taken from: https://realpython.com/python-web-scraping-practical-introduction/
    """
    print(e)


