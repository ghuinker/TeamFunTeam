from bs4 import BeautifulSoup
import certifi
import urllib3
import _thread
import time

class Crawler:

    def __init__(self):
        self.url_list = []
        self.http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    
    def add_url(self, url):
        self.url_list.append(url)
    
    def print_url_list(self):
        for txt in self.url_list:
            print(txt)

    def get_soup(self, url):
        veggies = self.http.request('GET', url)
        soup = BeautifulSoup(veggies.data, 'lxml')
        return soup

    def build_url_list(self):
        if len(self.url_list) is None:
            return None
        url = self.url_list.pop()
        soup = self.get_soup(url)
        url_len = len(url)
        
        for link in soup.find_all('a'):
            str = link.get('href')
            try:
                if len(str) > url_len and str[:url_len] == url and "comments" in str and "?sort" not in str:
                    self.url_list.append(str)
            except:
                continue

        

crawl = Crawler()
crawl.add_url('https://www.reddit.com/r/The_Donald/comments/5asj7o/announcement_you_know_we_are_winning_because_ctr/d9ixlqv/')
crawl.build_url_list()
crawl.print_url_list()
#soup = crawl.get_soup(url_list)


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
