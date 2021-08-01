import time

import webbrowser
import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher

#search engine so pulls up 10 first site if in google
def SearchAnything(subject):
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

        # to search
    query = subject[0]
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        print(j)

#open google with normal search
def webSearchNormal(subject):
    reconstru = reconstructString(subject, "+")
    openLink(reconstru)

#open google with normal image search
def imageSearch(subject):
    reconstru = reconstructString(subject, "+")
    url = "https://www.google.com/search?q=" + reconstru + "&client=firefox-b-d&source=lnms&tbm=isch&sa=X&biw=1920&bih=966"
    openLink(url)

#open google with normal video search
def vidSearch(subject):
    reconstru = reconstructString(subject, "+")
    url = "https://www.google.com/search?q="+ reconstru + "&client=firefox-b-d&source=lnms&tbm=vid&sa=X&biw=1920&bih=966"
    openLink(url)

#open google with normal map search (work on it)
def mapSearch(subject):
    reconstru = reconstructString(subject, "+")
    url = "https://www.google.com/maps/place/" + reconstru
    openLink(url)

#search bar youtube
def youtubeSearch(subject):
    reconstru = reconstructString(subject, "+")
    url = "https://www.youtube.com/results?search_query="+reconstru
    openLink(url)

#search in all movies and gives the ones with the most similarity
def StreamingSearch(subject, numSuggestion, LookalikeMin):
    start = time.time()
    movieName = reconstructString(subject, "-").lower()
    suggestion = []
    file = open("TextFiles/AllMovie.txt", "r")
    for line in file:
        #movieTitle = line.split(":", 1)[0]
        movieTitle = line
        if(similar(movieName, movieTitle) * 100 >= LookalikeMin):
            if len(suggestion) < numSuggestion:
                suggestion.append(line)
                sortin(movieName, suggestion)
            elif similar(movieName, movieTitle) > similar(movieName, suggestion[-1]):
                suggestion.pop()
                suggestion.append(line)
                sortin(movieName, suggestion)

    print(time.time() - start)
    return suggestion

#Sort the similar movie so the one with the highest similarity are first
def sortin(movieName, suggestion):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(suggestion) - 1):
            if similar(movieName, suggestion[i]) < similar(movieName, suggestion[i + 1]):
                # Swap the elements
                suggestion[i], suggestion[i + 1] = suggestion[i + 1], suggestion[i]
                # Set the flag to True so we'll loop again
                swapped = True

#fct reconstruc String to fit the need of each site
def reconstructString(toReconstruct, symboleMilieu):
    construct = ""
    for s in toReconstruct:
        construct += s + symboleMilieu
    return construct

#open link site
def openLink(url):
    webbrowser.open(url)

#fct put all movies on netflix and disney+ on a text file with the link
def LoadMovieStream():
    movies = open("TextFiles/AllMovie.txt", "w+")
    start = time.time()
    toSort = []
    #LoadNetflix needs 73 loop 2494
    toSort.extend(loadLoop(73, 'netflix'))
    #load disney+ need 18 loops
    toSort.extend(loadLoop(18, 'disney_plus'))
    toSort = list(set(toSort))
    toSort.sort()
    for w in toSort:
        #movies.write(w + ": " + movieLink(w) + "\n")
        movies.write(w + "\n")
    movies.close()
    print("TIMEEEEEE: " + str(time.time() - start))

#loop to go trough all the movies on reelgood (only for american movies) and take all the movie names
def loadLoop(numLoop, sourceStream):
    toSort = []
    for i in range(numLoop):
        num = 0
        src = []
        result = requests.get('https://reelgood.com/movies/source/' + sourceStream +'?offset=' + str(i * 50))
        src.append(result.content)
        soup = BeautifulSoup(src[0], 'lxml')
        urls = []
        for tags in soup.find_all("a"):
            if(str(tags).startswith('<a href="/movie/') and num % 2 == 1):
                name = str(tags)
                name = name.replace('<a href="/movie/', "")
                name = name.split('"', 1)[0]
                toSort.append(name)
            num = num + 1
    return toSort

#takes the movie name and pulls the link reelgood so american movies
def movieLink(name):
    print(name)
    src = []
    stringURLS = ""
    result = requests.get("https://reelgood.com/movie/" + str(name))
    src.append(result.content)
    soup = BeautifulSoup(src[0], 'lxml')
    urls = []
    for tags in soup.find_all("div"):
        a_tag = tags.find('a')
        if a_tag != None and ('https://www.netflix.com/watch/' in str(a_tag) or 'https://www.disneyplus.com/movies' in str(a_tag)):
            urls.append(a_tag.attrs['href'])
    urls = list(set(urls))
    for u in urls:
        print(u)
        stringURLS = stringURLS + str(urls[0]) + ", "
    return stringURLS

#checks similarity between 2 strings
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()