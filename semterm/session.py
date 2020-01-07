import pymorphy2 as morf

class Session:
	def __init__(self):
		self.dialogs = []

	def add_dialog(self, d):
		self.dialogs.append(d)

	def input(self, text, response=True):
		if len(self.dialogs) == 0:
			return "", 0.0

		responses = []
		for d in self.dialogs:
			r = d.input(text, response) 
			if r is None or len(r) != 2:
				print("Warn: dialog {} return is not valid".format(d.__class__))
			responses.append(r)

		return max(responses, key=lambda x: x[1])