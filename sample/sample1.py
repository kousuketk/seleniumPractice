from selenium import webdriver
import func

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
print(driver.title)

search_box = driver.find_element_by_name("q")
search_box.send_keys("sample input")
search_box.submit()
print(driver.title)
driver.save_screenshot("search_result.png")
func.print_search(driver)
driver.quit()
