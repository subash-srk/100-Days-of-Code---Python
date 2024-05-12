from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_no = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# print(article_no.text)

# article_no.click()

# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python", Keys.ENTER)