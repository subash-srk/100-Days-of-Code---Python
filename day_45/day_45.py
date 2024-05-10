from bs4 import BeautifulSoup
# import lxml

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)
# print(soup.prettify())
# print(soup.li)
all_tags = soup.find_all(name="a")
# print(all_tags)

for tag in all_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass

heading = soup.find(name="h1", id="name")
# print(heading)
head1 = soup.find(name="h3", class_="heading")
# print(head1)

select = soup.select_one(selector="p a")
select1 = soup.select_one(selector="#name")
# print(select1)

headings = soup.select(".heading")
print(heading)