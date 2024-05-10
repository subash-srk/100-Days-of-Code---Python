from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)
article_span = soup.find_all(name="span", class_="titleline")


articles = []

for article in article_span:
    article_each = article.find(name="a")
    articles.append(article_each)


article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(f"TITLE: {article_texts[largest_index]}")
print(f"LINK: {article_links[largest_index]}")
print(f"UPVOTES: {article_upvotes[largest_index]}")
