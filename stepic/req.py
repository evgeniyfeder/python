import requests
url = "https://stepic.org/media/attachments/course67/3.6.2/237.txt".strip()
r = requests.get(url)
print(len(r.text.splitlines()))
print(r.text)
