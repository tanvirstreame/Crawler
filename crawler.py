import bs4 as bs
import re
import urllib.request

sauce=urllib.request.urlopen("http://en.prothomalo.com/bangladesh/news/176492/Take-leave-join-Hasina%E2%80%99s-electioneering-in-next")
soup=bs.BeautifulSoup(sauce,'lxml')




#if "Bangladesh" in soup.find('p').text:
#    print(soup.find('p').text)



#if re.search('(?i)bangladesh', soup.find('p').text):
   # print(soup.find('p').text)


#print(soup.find_all('p')[1].text)
for par in soup.find_all('p'):
    if re.search('(?i)platform ', par.text):
        print(par.text)
