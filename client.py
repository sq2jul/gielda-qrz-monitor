import requests

class GieldaClient():
	def __init__(self):
		pass

	def getRawPage(self, page=0):
		if page > 0:
			url = "http://gielda.qrz.pl/default.asp?kat=0&nr_str=" + str(page)
		else:
			url = "http://gielda.qrz.pl/default.asp"
		resp = requests.get(url)
		if resp.status_code == 200:
			return resp.content
		return None
