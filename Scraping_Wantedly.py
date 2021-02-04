from bs4 import BeautifulSoup
import requests

url = 'https://www.wantedly.com/stories/tags/%E7%A7%81%E3%81%AE%E5%B0%B1%E6%B4%BB'

re = requests.get(url)
soup = BeautifulSoup(re.text, "lxml")
article_lists = soup.find_all('article', class_='stream-post')

for article in article_lists:
    title = article.find('h2', class_='article-title').get_text(strip=True)
    description = article.find('div', class_='article-description').get_text(strip=True)
    link = article.find('a').get('href')
    url = 'https://www.wantedly.com'+link
    print(title, description, url)
