from bs4 import BeautifulSoup
from advert import Advert, AdvertType

class TrAdvertParser():
	def __init__(self, rawTr):
		self._tr = rawTr

	def parse(self):
		if not self._tr:
			return None

		try:
			return self._getAdvert()
		except:
			return None

	def _getAdvert(self):
		type = self._parseAdvertType()
		id = self._parseId(type)
		titleTuple = self._parseTitleHref()
		title = titleTuple[0]
		link = titleTuple[1]
		thumbnail = self._parseThumbnail()
		description = self._parseDescription(type)

		return Advert(id, type, title, link, thumbnail, description)

	def _parseTitleHref(self):
		titleHref = self._tr.find("a", {"class": "tytul"})
		title = titleHref.get_text()
		link = "http://gielda.qrz.pl/" + titleHref['href']
		return (title, link)

	def _parseAdvertType(self):
		if self._tr.find("span", {"class": "kupie"}):
			return AdvertType.BUY
		if self._tr.find("span", {"class": "zamienie"}):
			return AdvertType.EXCHANGE
		return AdvertType.SELL

	def _parseId(self, type):
		return int(self._tr.find("i").find_all("b")[1].get_text())

	def _parseThumbnail(self):
		maybeImg = self._tr.find('img')
		if maybeImg:
			return "http://gielda.qrz.pl/" + maybeImg['src']
		return ''

	def _parseDescription(self, type):
		return self._tr.find("a", {"class": "tytul"}).parent.get_text(" ", strip=True)

class GieldaParser():
	def __init__(self):
		pass

	def parse(self, rawPage):
		soup = BeautifulSoup(rawPage, features="html.parser")
		trs = soup.select('body center table:nth-child(3) table:nth-child(2) tr:nth-of-type(even)')

		for tr in trs:
			advert = TrAdvertParser(tr).parse()
			if advert:
				yield advert
