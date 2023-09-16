import requests

print(requests.__version__)

ghp = requests.get("http://google.com")
print(ghp.text)


