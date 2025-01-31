from bs4 import BeautifulSoup as bs
import requests
import json


url = "http://www.foxnews.com/politics/obamacare-in-trouble-exchange-provision-delayed-as-lawmakers-push-to-repeal/"

#get article text from nbcnews url
def getArticleBody(url):
    # Make a GET request to fetch the raw HTML content
    html_content1 = requests.get(url).text

    # Parse the html content
    soup = bs(html_content1, "html.parser")

    #find element containing article text
    res = soup.head.find_all('script', {'type': 'application/ld+json'})

    #iterate through elements to find article text
    for item in res:
        json_data = json.loads(str(item.string))
        try:
            article_body = json_data['articleBody']
            return article_body
        except:
            continue

print(getArticleBody(url))