from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.seznam.cz/')
web = response.text
soup = BeautifulSoup(web, 'html.parser')

articles = soup.find_all(class_="article__title")

with open("webscrapping/projekt1/seznam.txt", "w") as file:
    for one_article in articles:
        one_article_text = one_article.getText()
        one_article_link = one_article.get("href")
        
        if "Fiala" in one_article_text or "Putin" in one_article_text:
            file.write(one_article_link)
            file.write(one_article_text)
            file.write("\n")