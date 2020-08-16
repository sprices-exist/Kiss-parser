from bs4 import BeautifulSoup

with open('history.html', encoding='UTF-16LE') as html_file:
    soup= BeautifulSoup(html_file, 'lxml')

manga=open("anime names.txt","w")
mangaLinks=open("anime names with links.txt","w")

mangaDict=[ ]

l=0

for link in soup.find_all('td'):
    if "kissanime.ru/Anime/" in link.text:
        temp=str(link.text)
        temp1=temp.replace("https://kissanime.ru/Anime/", "")
        temp2=temp1.replace("-", " ")
        head, sep, tail = temp2.partition('/')
        if head not in mangaDict:
            l+=1
            mangaDict.append(head)
            manga.write(str(l)+". " + head + "\n")
            mangaLinks.write(str(l) + ". " + head + " link-" + temp + "\n")

manga.close()
mangaLinks.close()

#made by Tanmay Nandanikar
    





