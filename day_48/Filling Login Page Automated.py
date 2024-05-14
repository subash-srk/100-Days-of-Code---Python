from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fName")
lname = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

fname.send_keys("Akira")
lname.send_keys("Kurasowa")
email.send_keys("kurasowa@gmail.com")

button = driver.find_element(By.CSS_SELECTOR, "button")
button.send_keys(Keys.ENTER)