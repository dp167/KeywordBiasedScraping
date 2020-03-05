#from google import google
import google
from googlesearch import search
import re
from textblob import TextBlob
import texttable as tt
from time import sleep

def search_web( query):
    query = query
    num_page = 3
    foxnews=0
    farright = 0
    middleright = 0
    middle = 0
    middleleft = 0
    farleft = 0
    #regex = re.compile('fox')A
    fox = "fox"
    dailywire = "dailywire"
    newyorkpost = "newyorkpost"
    washingtontimes = "washingtontimes"
    infowars = "infowars"


    search_results = []
    k = 0
    #search_results = search("inurl:" + site + " intext:" + search, 3)
    for i in search(query=query,tld='com',lang = 'en',num =10,start = 0, stop = None, pause = 2):
        search_results.append(i)
        print((k))
        k = k+1
        #print(type(i))
        #print(i)
    for j in search_results:
        print(j)
        if ((j.find(fox) > -1) or (j.find(dailywire)>-1) or (j.find(newyorkpost) > -1 ) or (j.find(washingtontimes)> -1) or j.find(infowars)>-1):
            farright = farright +1
        if(j.find("reuters")>-1)or j.find("bloomberg") >-1 or j.find("abc")>-1 or j.find("usatoday")>-1:
            middle = middle + 1
    print(farright)
    print(middle)

search_web("trump")
