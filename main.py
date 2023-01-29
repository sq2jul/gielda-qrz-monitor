from client import GieldaClient
from parser import GieldaParser

if __name__ == '__main__':
	c = GieldaClient()
	p = GieldaParser() 
	rawPage = c.getRawPage()
	adverts = p.parse(rawPage)
	for advert in adverts:
		print(advert)
