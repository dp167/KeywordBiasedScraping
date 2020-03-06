#from google import google
import google
from googlesearch import search
import plotly.graph_objects as go
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
        if ((j.find("fox") > -1) or (j.find("dailywire")>-1) or (j.find("newyorkpost") > -1 ) or (j.find("washingtontimes")> -1) or j.find("infowars")>-1):
            farright = farright +1
        if(j.find("reuters")>-1)or j.find("bloomberg") >-1 or j.find("abc")>-1 or j.find("usatoday")>-1:
            middle = middle + 1
        if(j.find("npr")>-1)or (j.find("bbc")>-1)or (j.find("nbc")>-1) or (j.find("washingtonpost")>-1) or (j.find("politico")>-1)or (j.find("guardian")>-1)or (j.find("newyorktimes")>-1)or (j.find("newyorker")>-1)or (j.find("")>-1):
           middleleft = middleleft + 1
        if(j.find("huffington")>-1)or (j.find("buzz")>-1)or (j.find("msnb")>-1) or (j.find("slate")>-1):
            farleft = farleft+1
    print(farright)
    print(middle)
    print(farleft)

    fig = go.Figure(
        data=[go.Bar(y=[farleft, middle, farright])],
        layout_title_text="A Figure Displaying political bias from left to right"
    )
    fig.show(renderer="png")

search_web("corona")
