import requests

result = requests.get("http://docs.python.org")
print(result.status_code)
assert result.status_code == 200 
print(result.text)
assert "Copyright" in result.text
