import requests

class GieldaClient():
	def __init__(self):
		pass

	def getRawPage(self):
		resp = requests.get('http://gielda.qrz.pl/')
		if resp.status_code == 200:
			return resp.content
		return None
