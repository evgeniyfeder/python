import requests

def get_text(file_name):
	r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + file_name)
	r = r.text
	return r

r = get_text("699991.txt")

with open('text.out', 'w') as outf:
	for i in range(250):
		r = get_text(r)
		print(r)
		outf.write(r + '\n')