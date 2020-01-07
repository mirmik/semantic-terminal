import pymorphy2
import os

morph = pymorphy2.MorphAnalyzer()

def morph_analize(arg):
	return morph.parse(arg)

class Session:
	def __init__(self):
		self.dialogs = []
		self.debug_mode = False

	def add_dialog(self, d):
		self.dialogs.append(d)

	def set_debug_mode(self, en):
		if en:
			self.debug_mode = True
			for d in self.dialogs:
				d.debug_mode = True

	def parse(self, text):
		parr = []
		for t in text.split():
			parr.append(morph.parse(t))
		return parr

	def input(self, text):
		stdparse = self.parse(text)
		if self.debug_mode:
			print("stdparse:", stdparse)

		if len(self.dialogs) == 0:
			return "", 0.0

		responses = []
		for d in self.dialogs:
			confidence = d.input(text) 
			responses.append((d,confidence))

		if self.debug_mode:
			print("RESPONCES:")
			for r in responses:
				print(r)

		winner = max(responses, key=lambda x: x[1])

		if self.debug_mode:
			print("WINNER:")
			print(winner)

		if winner[1] < 0.7:
			print("Неудалось распознать ввод.")

		else:
			winner[0].apply()