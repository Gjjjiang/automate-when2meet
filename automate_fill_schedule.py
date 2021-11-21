from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.when2meet.com/?13706256-dnJuv")
assert "When2meet" in driver.title

name = "participant"
password = "password"

# pre-fill first page
elem = driver.find_element_by_id("name")
elem.clear()
elem.send_keys(name)

elem = driver.find_element_by_id("password")
elem.clear()
elem.send_keys("password")
elem.send_keys(Keys.TAB)
elem.send_keys(Keys.ENTER)

button = driver.find_element(By.XPATH, "//input[@value='Sign In']")
# button = driver.find_element_by_xpath("//div[@id='SignIn']/input[1]")
# click(button)

# wait until we're on the schedule-view page
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "YouGridSlots"))
    )
except:
    driver.quit()

# now we can fill in the schedule based on what we got off Teams or Google calendar
datetime1 = "YouTime1637514000" #dummy data to be replaced
datetime2 = "YouTime1637541900" #more dummy data

source = driver.find_element(By.ID, datetime1)
target = driver.find_element(By.ID, datetime2)
button = driver.find_element(By.ID, datetime1)
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(button).click(button).perform()
actions = ActionChains(driver)
actions.drag_and_drop(source, target)
actions.perform()

assert "No results found." not in driver.page_source
# driver.close()
