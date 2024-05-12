from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"Price is: {price_dollar.text}.{price_cents.text}")

search_bar = driver.find_element(By.NAME, "q")
print(search_bar.get_attribute("name"))

bug_element = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_element.text)

driver.quit()
# driver.close()
