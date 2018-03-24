from bs4 import BeautifulSoup
import certifi
import urllib3

class Crawler:

    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    

    """
    url_list.append('https://www.reddit.com/r/Showerthoughts/comments/86pkzc/the_most_unrealistic_thing_about_spongebob_is/')
    url_list.append('https://www.reddit.com/r/The_Donald/')
    """

    def __init__(self):
        self.url_list = []
    
    def add_url(self, url):
        self.url_list.append(url)
    
    def print_url_list(self):
        for txt in self.url_list:
            print(txt)

    def get_soup(self, url_list):
        url = url_list.pop()
        veggies = http.request('GET', url)
        soup = BeautifulSoup(veggies.data, 'lxml')
        return soup

    def build_url_list(self, start_url):
        soup = get_soup(self.url_list)
        for link in soup.find_all('a'):
            print(link.get('href'))


crawl = Crawler()
crawl.add_url('https://www.reddit.com/r/Showerthoughts/comments/86pkzc/the_most_unrealistic_thing_about_spongebob_is/')
crawl.build_url_list(
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
