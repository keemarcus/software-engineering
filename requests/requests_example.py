import requests

from bs4 import BeautifulSoup

def test_python_org_has_copyright():
    result = requests.get("http://python.org")
    assert result.status_code == 200 
    assert "Copyright" in result.text

def test_python_org_has_a_donate_button():
    result = requests.get("http://python.org")
    assert result.status_code == 200 
    page = BeautifulSoup(result.text, 'html.parser')
    donate_button = page.find("a",class_="donate-button")
    assert donate_button
    assert donate_button.string == "Donate"
  
def test_python_org_search_for_max_returns_several_items():
    result = requests.get("https://www.python.org/search/?q=max")
    assert result.status_code == 200 
    page = BeautifulSoup(result.text, 'html.parser')
    main_content = page.find("section",class_="main-content")
    assert main_content, "Main content section not found"
    list_items = main_content.find_all("li")
    print(len(list_items))
    assert len(list_items) > 3
    for list_item in list_items:
        print(list_item("p")[0].string)
  
def test_amazon_blender_contains_oster():
      headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
      }
      result = requests.get("https://www.amazon.com/s?k=blender", headers=headers)
      print(result.status_code)
      print(result.text)
      assert "Oster" in result.text
  
# def get_tasks():
#     result = requests.get("http://swift-keemarcus.pythonanywhere.com")
#     # print(result.status_code)
#     assert result.status_code == 200 
#     print(result.text)
#     print(soup.prettify())
#     #temp_p = htmlparser.p["myforecast-current-lrg"]
#     #print(temp_p)
#     #return temp

if __name__ == "__main__":
    test_python_org_has_copyright()
    test_python_org_has_a_donate_button()
    test_python_org_search_for_max_returns_several_items()
    #test_amazon_blender_contains_oster()
    print("done.")
