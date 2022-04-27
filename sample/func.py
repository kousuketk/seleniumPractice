import time


def init_search(driver):
    driver.get("https://www.google.com/")
    search_box = driver.find_element_by_name("q")
    search_box.send_keys("sample input")
    search_box.submit()
    print(driver.title)
    driver.save_screenshot("search_result.png")


def print_title(driver):
    for g_h3 in driver.find_elements_by_css_selector(".g h3"):
        print(g_h3.text)


def print_all(driver):
    for i, g in enumerate(driver.find_elements_by_class_name("g")):
        print("----------- " + str(i + 1) + " -----------")
        print(g.find_element_by_tag_name("h3").text)
        print("\t" + g.find_element_by_tag_name("a").get_attribute("href"))
        print("\t" + g.find_element_by_class_name("VwiC3b").text)


def print_search(driver):
    search_query = driver.find_element_by_name("q")
    print(search_query.get_attribute("value"))


def print_last_article(driver, actions):
    el = driver.find_elements_by_css_selector(".g h3")[-1]
    actions.move_to_element(el).perform()
    print(el.text)
    time.sleep(5)


def get_window_size(driver):
    print(driver.get_window_size())
    print(
        driver.execute_script("return window.innerWidth;"),
        driver.execute_script("return window.innerHeight;"),
    )
    print(
        driver.execute_script("return window.outerWidth;"),
        driver.execute_script("return window.outerHeight;"),
    )
