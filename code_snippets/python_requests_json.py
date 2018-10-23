import requests

url = 'https://status.github.com/api/status.json'
url = 'http://www.example.com'
resp = requests.get(url)


print type(resp)
print type(resp.text)
print resp.text

x = resp.json()
print x['status'], x['last_updated']
