import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/') # gets the website and stores in object
res2 = requests.get('https://news.ycombinator.com/news?p=2')
# print(res.text) # displays the html text of the website as a string

soup = BeautifulSoup(res.text, 'html.parser') # converts website from string actual html
soup2 = BeautifulSoup(res2.text, 'html.parser')
# print(soup.find_all('a')) # provides all the links on the website as a list
# print(soup.body) # provides the <body> of the website
# print(soup.find(id = '43613180')) # finding specific id's from website
links = soup.select('.titleline') # takes the title of articles
subtext = soup.select('.subtext') # takes the # of points for each article

links2 = soup2.select('.titleline')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k: k['votes'], reverse=True)

def create_custom_link(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        a_tag = item.select_one('a')
        href = a_tag.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
        if points > 99:
            hn.append({'title': title, 'link': href, 'votes': points})

    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_link(mega_links, mega_subtext))



