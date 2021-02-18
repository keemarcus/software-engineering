from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

tasks_url = "http://swift-keemarcus.pythonanywhere.com"

def test_has_correct_columns():
    driver = webdriver.Chrome()
    try:
        driver.get(tasks_url)
        header_elements = driver.find_elements_by_tag_name("h1")
        assert len(header_elements) > 0
        column_titles = [e.text for e in header_elements]
        assert column_titles[0] == "Today"
        assert column_titles[1] == "Tomorrow"
        assert column_titles[2] == "Later"
        assert column_titles[3] == "Probably Never"
    except Exception as e:
        driver.close()
        raise e
    driver.close()

if __name__ == "__main__":
    test_has_correct_columns()
