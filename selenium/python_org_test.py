from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_searchbox_finds_something():
    driver = webdriver.Chrome()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    print(driver.page_source)
    assert "No results found." not in driver.page_source
    driver.close()

def test_have_an_about_link():
    driver = webdriver.Chrome()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    about_element = driver.find_element_by_id("about")
    assert "About" in about_element.text
    driver.close()

if __name__ == "__main__":
    test_have_an_about_link()