import requests

print(requests.__version__)

ghp = requests.get("http://google.com")
#print(ghp.text)

github_code = requests.get("https://raw.githubusercontent.com/vamsiv2001/cmput404-lab1/main/script.py")
print(github_code.text)

