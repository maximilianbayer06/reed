import requests
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse


def TheGuardian():
    Information = []

    response = requests.get('https://www.theguardian.com/international')
    soup = BeautifulSoup(response.text, 'html.parser')

    Info = soup.find('section', attrs={'id':'headlines'})
    TopInfo = soup.find('section', attrs={'id':'most-viewed'})

    Articles = Info.find_all('a',attrs={'data-link-name': 'article', 'class': 'u-faux-block-link__overlay js-headline-text'})
    TopArticles = TopInfo.find_all('a',attrs={'data-link-name': 'article', 'class': 'u-faux-block-link__overlay js-headline-text'})


    for article in TopArticles:
        title = article.text
        title = str(title).replace("‘", "'")
        title = str(title).replace("’", "'")
        title = str(title).replace("–", "-")
        title = title.replace('$', '(dollar)')
        title = title.replace('.', '(dot)')
        title = title.replace(',', '(comma)')
        title = str(title).strip()
        img = bingImageSearch(title)
        link = article.get('href')
        Information.append([title, link, img])


    for article in Articles:
        title = article.text
        title = str(title).replace("‘", "'")
        title = str(title).replace("’", "'")
        title = str(title).replace("–", "-")
        title = title.replace('$', '(dollar)')
        title = title.replace('.', '(dot)')
        title = title.replace(',', '(comma)')
        title = str(title).strip()
        img = bingImageSearch(title)
        link = article.get('href')
        Information.append([title, link, img])

    return Information


def WashingtonPost():
    Information = []

    response = requests.get('https://www.washingtonpost.com/latest-headlines/?itid=hp_latest-headlines_p003')
    soup = BeautifulSoup(response.text, 'html.parser')

    Articles = soup.findAll('div', attrs={'data-feature-id':'homepage/story'})

    for element in Articles:
        content = element.find('div', attrs={'class':'story-headline pr-sm'})
        image = element.find('div', attrs={'class':'border-box pl-0 w-100'})
        
        link = element.find('a')
        link = link.get('href')

        title = content.find('h3', attrs={'class': 'font-md font-bold font--headline lh-sm gray-darkest hover-blue mb-0 antialiased mb-xxs'})
        title = str(title.text).replace("‘", "'")
        title = str(title).replace("—", "-")
        title = title.replace('$', '(dollar)')
        title = title.replace('.', '(dot)')
        title = title.replace(',', '(comma)')
        img = bingImageSearch(title.replace("’", "'"))

        Information.append([title, link, img])

    return Information

def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(
        urllib.request.Request(url,headers=header)),
        'html.parser')

def bingImageSearch(query):
    query = str(query).replace("(dot)", ".")
    query = str(query).replace("(dollar)", "$")
    query = str(query).replace("(comma)", ",")
    query= query.split()
    query='+'.join(query)
    url="http://www.bing.com/images/search?q=" + query + "&FORM=HDRSC2"
    #print(url)

    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    soup = get_soup(url,header)


    image_result_raw = soup.find("a",{"class":"iusc"}).find('img')

    image = image_result_raw.get('src')

    return image

    

def CNN():
    Information = []

    response = requests.get('https://edition.cnn.com/world')
    soup = BeautifulSoup(response.text, 'html.parser')

    Articles = soup.findAll('a', attrs={'class':'container__link container_grid-4__link'})
    for element in Articles:

        link = element.get('href') 
        link = "https://edition.cnn.com/" + str(link)
        title = element.find('div', attrs={'class': 'container__headline container_grid-4__headline'})
        title = title.text
        title = str(title).strip()
        title = title.replace('$', '(dollar)')
        title = title.replace('.', '(dot)')
        title = title.replace(',', '(comma)')

        img = element.find('source')
        img = str(img.get('srcset')).replace("amp;", "")

        Information.append([title, link, img])

    return Information


def bingNews():
    Information = []

    response = requests.get('https://www.bing.com/news/search?q=Top+stories&setmkt=en-us')
    soup = BeautifulSoup(response.text, 'html.parser')

    Articles = soup.findAll('a', attrs={'class':'news_fbcard wimg'})
    for element in Articles:
        link = element.get('href')
        title = element.find('div', attrs={'class': 'na_t news_title ns_big'})
        title = title.text
        title = title.replace('$', '(dollar)')
        title = title.replace('.', '(dot)')
        title = title.replace(',', '(comma)')
        
        image = element.find('img', attrs={'class': 'rms_img'})
        if image != None:
            image = image.get('data-src-hq')

            Information.append([title,link, img])

    return Information

def News():
    info1 = bingNews()
    info2 = CNN()
    info3 = WashingtonPost()
    info4 = TheGuardian()

    info = []
    info.append(info1)
    info.append(info2)
    info.append(info3)
    info.append(info4)

    return info
