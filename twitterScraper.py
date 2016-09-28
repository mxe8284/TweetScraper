import urllib
import csv
import urllib.request
from bs4 import BeautifulSoup
import time



# store url info
theurl = " "  # insert URL here
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage, "html.parser")

tweet_list = []

# to clean html code add '.text' to title
print(soup.title.text)
print("")

# for link in soup.findAll('a'):
#    print(link.get('href'))
# print(soup.find('div', {"class":"ProfileHeaderCard"}).find('p').text)

i = 1
for tweets in soup.findAll('div', {"class": "content"}):
    print("")
    print (i, tweets.find('p').text)
    i = i+1
    tweett = tweets.find('p').text
    d = {'tweett': tweett}
    tweet_list.append(d)


with open(' .csv', 'w') as csvfile:   # CREATE filename here
    fieldnames = ['TWEETS']           # tweetlist[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for tweet in tweet_list:
        writer.writerow(tweet)