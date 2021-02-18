import requests

# result = requests.get("http://docs.python.org")
# print(result.status_code)
# assert result.status_code == 200 
# print(result.text)
# assert "Copyright" in result.text

from bs4 import BeautifulSoup

def get_temp_at_walsh():
    result = requests.get("https://forecast.weather.gov/MapClick.php?textField1=40.8848&textField2=-81.4035#.YCvTfRNKhTY")
    # print(result.status_code)
    assert result.status_code == 200 
    # print(result.text)
    lines = result.text.split("\n")
    temp = ""
    for line in lines:
        if "myforecast-current-lrg" in line:
            for c in line:
                if c.isdigit():
                    temp = temp + c
    return temp

def get_temp_at_walsh2():
    result = requests.get("https://forecast.weather.gov/MapClick.php?textField1=40.8848&textField2=-81.4035#.YCvTfRNKhTY")
    # print(result.status_code)
    assert result.status_code == 200 
    print(result.text)
    soup = BeautifulSoup(result.text, 'html.parser')
    print(soup.prettify())
    #temp_p = htmlparser.p["myforecast-current-lrg"]
    #print(temp_p)
    #return temp

def get_tasks():
    result = requests.get("http://swift-keemarcus.pythonanywhere.com")
    # print(result.status_code)
    assert result.status_code == 200 
    print(result.text)
    soup = BeautifulSoup(result.text, 'html.parser')
    print(soup.prettify())
    #temp_p = htmlparser.p["myforecast-current-lrg"]
    #print(temp_p)
    #return temp


#print("It is ",get_temp_at_walsh2(),"degrees outside.")
get_tasks()