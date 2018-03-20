

class Tile:
	SYMBOLS = {
		'box':'U+13FF',
		'latin-ain':'U+1D25',
		'sideways-u':'U+1D1E',
		'??':'U+2047',
		'?!':'U:2048',
		'!?':'U:2049'
	}
	def __init__(symbol,name):
		self._symbol = Tile.SYMBOLS[symbol] 
		self._name = name 
		self._desc = {}
		self._bg = 'black' 
		self._fg = 'white'

	def summary(self,desc=None):
		if not desc is None:
			self._desc = desc 

		return self._desc


class FunTile(Tile):

	def __init__(symbol,name):
		Tile.__init__(symbol,name)

class WorkTile(Tile):

	def __init__(symbol,name):
		Tile.__init__(symbol,name)



def radio():
	tiles = []
	prof = RadioTile('det','Profanity Detector')
	tb = RadioTile('tb','Trackblaster Converter')
	cue = RadioTile('cue','Cue File Converter')
	itunes = RadioTile('itunes','ITunes Converter')
	return tiles 


def tool():
	tiles = []
	mtg = ToolTile('rename','Column Rename')


def fun1():
	tiles = []
	mtg = FunTile('fem','Meeting Simulator')
	scr = FunTile('mix','Scramble')
	spy = FunTile('rus','TV Time')	
	rnd = FunTile('pokernd','Pokemon Randomizer')

	return [mtg,scr,spy,rnd] 



