from enum import Enum

class AdvertType(Enum):
	SELL = 'sprzedam'
	BUY = 'kupie'
	EXCHANGE = 'zamienie'

	def __str__(self):
		return self.value

class Advert():
	def __init__(self, id, type, title, link, thumbnail, description):
		self.id = id
		self.type = type
		self.title = title
		self.link = link
		self.thumbnail = thumbnail
		self.description = description

	def __str__(self):
		return 'Advert(id=' + str(self.id) + ',type=' + str(self.type) + ',title=' + self.title + ',link=' + self.link + ',thumbnail=' + self.thumbnail + ',description=' + self.description + ')'
