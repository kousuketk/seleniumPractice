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
