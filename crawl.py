import requests
from BeautifulSoup import BeautifulSoup

url = "http://www.omie.es/aplicaciones/datosftp/datosftp.jsp?path=/marginalpibc/"
#url ="http://www.omie.es/aplicaciones/datosftp/datosftp.jsp?path=/phf_stota/"
response = requests.get(url)
# parse html
page = str(BeautifulSoup(response.content))


def getURL(page):
    """

    :param page: html of web page (here: Python home page) 
    :return: urls in that page 
    """
    start_link = page.find("a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

text_file = open("OMEI_mlinks.txt", "w")

#text_file = open("OMEI_stota_links.txt", "w")
while True:
    url, n = getURL(page)
    page = page[n:]
    c = url.split(".")
    #print(url)
    if url:
        #print url
        text_file.write(url+'\n')

#        r= requests.get(url)
        #text = r.text.split(";")
        #print text
        #break
    else:
        break

text_file.close()