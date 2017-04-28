import requests

def getPage(url):
    response = requests.get(url)
    return response.content.decode("utf-8")

def getLink(page):

    startLink  = page.find('<a href=')
    if(startLink != -1):
        startQuote = page.find('"', startLink)
        endQuote   = page.find('"', startQuote+1)
        url        = page[startQuote+1 : endQuote]
    else:
        url = None
        endQuote = None

    return url,endQuote

def getAllLinks(page):
    links = []
    while(True):
        url, endQuote = getLink(page)
        if(url):
            links.append(url)
            page = page[endQuote+1:]
        else:
            break
    return links

def union(a,b):
    for n in b:
        if(n not in a):
            a.append(n)
    return a

def crawlWeb(url):
    tocrawl = [url]
    crawled = []
    # index   = [] #Modifying it to Dictionary Type Data Structure
    index = {}
    graph = {}
    for link in tocrawl:
        tocrawl.remove(link)
        if(link not in crawled):
            content = getPage(link)
            addPageToIndex(index, link, content)
            outgoingLinks = getAllLinks(content)
            graph[link] = [outgoingLinks]
            union(tocrawl,outgoingLinks)
            crawled.append(link)

    return crawled, index, graph

#Using List Structure
# def addToIndex(index, keyword, url):
#     for entry in index:
#         if(entry[0] == keyword):
#             entry[1].append(url)
#             return index
#     list = [keyword, [url]]
#     index.append(list)
#
#     return index

'''
    Modifying the addToIndex procedure
    using the Dictionary Data Structure
'''
def addToIndex(index, keyword, url):
    if keyword in index:
        index[keyword] = url
    else:
        index[keyword] = url

index = []
# print(addToIndex(index, 'udacity', 'http://www.udacity.com'))
# print(addToIndex(index, 'udacity', 'http://www.ncm.com'))
# print(addToIndex(index, 'computing', 'http://www.abc.com'))

#Lookup Using the List Structure
# def lookup(keyword, index):
#     for entry in index:
#         if(entry[0] == keyword):
#             return entry[1]
#     return []
'''
    Modifying the Lookup procedure using
    the Dictionary Data Structure
'''
def lookup(keyword, index):
    if keyword in index:
        return index[keyword]
    else:
        return []
# print(lookup('udacitys', index))

def addPageToIndex(index, url, content):
    words = content.split()
    for word in words:
        addToIndex(index, word, url)
    return index

# print(addPageToIndex(index, 'fake.test', 'This is a test'))
# print(addPageToIndex(index, 'real.test', 'This is not a test'))
# print(lookup('is', index))



# print(getAllLinks(getPage('http://www.ekantipur.com')))
crawled, index, graph = crawlWeb('https://www.udacity.com/cs101x/index.html')
# print(crawlWeb('https://www.cs101.udacity.com/urank/index.html'))
print(graph)

def computeURank(graph):
    d = 0.8 #damping factor. It is the probability that crawler with continue with the previous link than starting with new one
    numLoops = 10 #no of times page rank is calculated
    ranks = {}
    nPages = len(graph)
    for page in graph:
        ranks[page] = 1.0/nPages


    for i in range(0,nPages):
        newRanks = {}
        for page in graph:
            newRank = (1-d)/nPages
            for node in graph:
                if page in graph[node]:
                    newRank += d * (ranks[node]/ len(graph[node]))
            newRanks[page] = newRank
        ranks = newRanks
    return ranks



print(computeURank(graph))
