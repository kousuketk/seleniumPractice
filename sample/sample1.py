from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import func

driver = webdriver.Chrome()
actions = ActionChains(driver)
func.init_search(driver)
func.get_window_size(driver)
driver.quit()
