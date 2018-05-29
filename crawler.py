import bs4 as bs
import re
import urllib.request


urlText=input("Insert URl : ")
searchText=input("keyword :")
sauce=urllib.request.urlopen(urlText)
soup=bs.BeautifulSoup(sauce,'lxml')




#if "Bangladesh" in soup.find('p').text:
#    print(soup.find('p').text)



#if re.search('(?i)bangladesh', soup.find('p').text):
   # print(soup.find('p').text)


#print(soup.find_all('p')[1].text)
   
print("From h1")
for par in soup.body.find_all('h1'):
    if searchText.lower() in par.text.lower() :
        print(par.text)

print("From a")
for par in soup.body.find_all('a'):
    if searchText.lower() in par.text.lower() :
        print(par.text)
        
print("From p")
for par in soup.body.find_all('p'):
    if searchText.lower() in par.text.lower() :
        print(par.text)   

    
