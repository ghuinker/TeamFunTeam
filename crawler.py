from bs4 import BeautifulSoup
import certifi
import urllib3
import time
from bintrees import FastAVLTree

class Crawler:

    def __init__(self):
        self.url_list = []
        self.http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    
    def add_url(self, url):
        self.url_list.append(url)
    
    def get_url_list_size(self):
        return len(self.url_list)
    
    def print_url_list(self):
        for txt in self.url_list:
            print(txt)

    def get_soup(self, url):
        veggies = self.http.request('GET', url)
        soup = BeautifulSoup(veggies.data, 'lxml')
        return soup

    def build_url_list(self):
        if len(self.url_list) is None :
            return None
        url = self.url_list.pop(0)
        soup = self.get_soup(url)
        url_len = len(url)
        for link in soup.find_all('a'):
            str = link.get('href')
            try:
                if len(str) > url_len and str[:url_len] == url and "comments" in str and "?sort" not in str:
                    self.url_list.append(str)
            except:
                continue

    def get_comment_list(self):
        if len(self.url_list) is None:
            return
        self.build_url_list()
        count = self.get_url_list_size()
        for i in range(1):                      # DON'T FORGET TO CHANGE BACKT TO THE VARIABLE 'count'
            self.build_url_list()
            time.sleep(1)

    def get_comments(self):
        tree = FastAVLTree()
        if len(self.url_list) is None :
            return None
        url = self.url_list.pop(0)
        soup = self.get_soup(url)
        message_list = []
        for txt in soup.find_all('p') :
            str = txt.string
            if str != None :
                message_list.append(str)
        return message_list;

crawl = Crawler()
crawl.add_url('https://www.reddit.com/r/Showerthoughts/')
crawl.get_comment_list()
#crawl.print_url_list()
print(crawl.get_comments())



"""
print("\n\n\n\n--------------------------------------------------------\n\n\n\n")

print(soup.prettify())

print("\n\n\n\n--------------------------------------------------------\n\n\n\n")

# gives best options to search parameters
for txt in soup.find_all('dd') :
    print(txt.prettify())

print("\n\n\n\n--------------------------------------------------------\n\n\n\n")

message_list = ""

# gets the messages in all </p> comments by users
for txt in soup.find_all('p') :
    str = txt.string
    if str != None :
        message_list = message_list + "\n" + str

    

message_list = message_list + "\nEOF"
print(message_list)

print("\n\n\n\n--------------------------------------------------------\n\n\n\n")
"""
