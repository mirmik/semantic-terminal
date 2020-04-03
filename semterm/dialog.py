import abc
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

class Dialog:
	def __init__(self):
		self.debug_mode = False

	def first_verb(self, sents):
		for t in sents:
			if t[0].tag.POS in ( "VERB", "INFN" ):
				return t[0]
		return None

	def first_noun(self, sents):
		for t in sents:
			print(t[0].tag.__class__)
			if t[0].tag == pymorphy2.tagset.OpencorporaTag('LATN') or t[0].tag.POS == "NOUN" :
				return t[0]
		return None

	def input(self, text):
		sents = self.parse(text)
		confidence = self.estimate(sents)
		return confidence

	def parse(self, text):
		parr = []
		for t in text.split():
			parr.append(morph.parse(t))
		return parr

	def estimate(self, sents):
		return 0.0