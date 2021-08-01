import time
import requests
from bs4 import BeautifulSoup
#-------------------------------------------NETFLIX----------------------------------------------------
def LoadLinkstoSite():
    toSort = []
    #finds num loop needed to have checked all the movies
    numLoop = numLoopFilm()
    for x in range(1,int(numLoop)+1):
        src = []
        path = 'https://www.onnetflix.ca/type/movie?p=' + str(x)
        result = requests.get(path)
        src.append(result.content)
        soup = BeautifulSoup(src[0], 'lxml')
        for tags in soup.find_all("a"):
            if(str(tags).startswith('<a href="/') and 'title="' in str(tags)):
                name = str(tags)
                name = name.replace('<a href="/', "")
                name = name.split('"', 1)[0]
                toSort.append(name)
        print("FirstCharge " + str(x) + "/" + str(numLoop))
    return toSort

#search num total pages on site
def numLoopFilm():
    toSort = []
    src = []
    i = 0
    result = requests.get("https://www.onnetflix.ca/type/movie?p=1")
    src.append(result.content)
    soup = BeautifulSoup(src[0], 'lxml')
    for tags in soup.find_all("a"):
        if (str(tags).startswith('<a class="btn btn-success" href="/type/movie?p=') and i < 2):
            num = str(tags)
            num = num.replace('<a class="btn btn-success" href="/type/movie?p=', "")
            num = num.split('"', 3)[0]
            toSort.append(num)
            i = i + 1
    return toSort[1]

#Function to run
def writeMovieTextFile():
    t = time.time()
    notFound = []
    tosort = []
    movies = open("Canada/AllMovieNetflixCan.txt", "w+")
    listLink = LoadLinkstoSite()
    i = 1
    leng = len((listLink))
    for link in listLink:
        src = []
        path = 'https://www.onnetflix.ca/' + str(link)
        result = requests.get(path)
        src.append(result.content)
        soup = BeautifulSoup(src[0], 'lxml')
        for tags in soup.find_all("a"):
            if (str(tags).startswith('<a class="uline" href="') and "Play now" in str(tags)):
                linkNetflix = str(tags)
                linkNetflix = linkNetflix.replace('<a class="uline" href="http://www.netflix.com/WiPlayer?movieid=', "")
                linkNetflix = linkNetflix.split('"', 1)[0]
                linkNetflix = 'https://www.netflix.com/watch/' + linkNetflix
                name = link.split("/", 1)[0]
                try:
                    tosort.append(name + " " + linkNetflix + "\n")
                    #movies.write(name + " " + linkNetflix + "\n")
                except:
                    notFound.append(linkNetflix)
        print("SecondCharge " + str(i) + "/" + str(leng))
        i = i + 1
    print(time.time() - t)
    for name in tosort:
        movies.write(name)
    print(notFound)

    movies.close()

#---------------------------------------------------DISNEY PLUS----------------------------------------------------

def nameMovies():
    movies = open("AllMovieDisneyPlusCan.txt", "w+")
    i = 1
    start = time.time()
    toSort = []
    toSort.extend(loadLoop(1, 'disney_plus'))
    toSort.sort()
    for w in toSort:
        print(str(i) + "/" + str(len(toSort)))
        try:
            movies.write(w + ": " + movieLink(w) + "\n")
        except:
            print("movie " + w + " Not Found")
        i = i + 1
    movies.close()
    print("TIMEEEEEE: " + str(time.time() - start))
    #print(toSort)

def movieLink():
    src = []
    name = ""
    good = []
    notGood = []
    stringURLS = ""
    result = requests.get("https://www.wildaboutmovies.com/features/disney-plus-complete-list-of-movies/")
    src.append(result.content)
    soup = BeautifulSoup(src[0], 'lxml')
    urls = []
    _name = ""
    for tags in soup.find_all("p"):
        if str(tags).startswith('<p>•') or str(tags).startswith('•'):
            name = str(tags)
            for n in name.split("•"):
                #print("__")
                #print(n)
                #print("^^")
                if n.endswith("</p>"):
                    _name = n.replace('</p>', '')
                    #print(_name)
                elif n.endswith('<br/>\n'):
                    _name = n.replace('<br/>\n', '')
                    #print(_name)

                #print(_name)
                #print("^^^")
                if(_name.startswith(" <a href")):
                    _name = n.split('">')[1]
                    _name = _name.replace('</a>', '')
                    _name = _name.replace("<br/>", "")
                    good.append(_name)
                else:
                    good.append(_name)
                _name = ""
    good.remove("")
    bla = ""
    for n in good:
        bla = n
        if n.endswith("\n") or n.startswith("\n"):
            bla = n.replace("\n", "")
        if bla.startswith(" "):
            bla = bla[1:]
            #print(bla)
        notGood.append(bla)

    for n in notGood:
        if n == "":
            pass
        else:
            remakeForSite(n)

    return stringURLS

def remakeForSite(n):
    recon = ""
    name, year = n.split("(")
    year = year[:-1]
    for part in name.split():
        recon = recon + part + "-"
    recon = recon + year
    recon = recon.lower()
    recon.replace(":", "")
    print(recon)
    #print(year)

movieLink()