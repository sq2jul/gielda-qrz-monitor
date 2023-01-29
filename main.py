from client import GieldaClient
from parser import GieldaParser
from optparse import OptionParser

if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option("-p", "--page", dest="page", help="nr strony giełdy do sparsowania", metavar="PAGE", type="int")
	(options, args) = parser.parse_args()

	c = GieldaClient()
	p = GieldaParser() 
	rawPage = c.getRawPage(page=options.page)
	adverts = p.parse(rawPage)
	for advert in adverts:
		print(advert)
